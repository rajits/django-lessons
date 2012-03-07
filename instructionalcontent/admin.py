from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from genericcollection import GenericCollectionTabularInline

from models import *
from settings import RELATION_MODELS, JAVASCRIPT_URL, REQUIRED_FIELDS

from tinymce.widgets import TinyMCE
from concepts.admin import ConceptItemInline

class VocabularyInline(admin.TabularInline):
    model = Vocabulary
    raw_id_fields = ('glossary_term',)

class QuestionAnswerInline(admin.TabularInline):
    model = QuestionAnswer

class ResourceInline(admin.TabularInline):
    model = ResourceItem
    raw_id_fields = ('resource',)

if RELATION_MODELS:
    class ActivityFormSet(forms.models.BaseInlineFormSet):
        def get_queryset(self):
            'Returns all LessonRelation objects which point to our Lesson'
            return [x for x in super(ActivityFormSet, self).get_queryset()
                if x.content_type.app_label + '.' + x.content_type.model in RELATION_MODELS]

    class InlineActivityRelation(GenericCollectionTabularInline):
        model = ActivityRelation
        formset = ActivityFormSet

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        for field in REQUIRED_FIELDS:
            field_name = field[0]
            app_label, model = field[1].split('.')
            ctype = ContentType.objects.get(app_label=app_label, model=model)
            self.fields[field_name] = forms.ModelChoiceField(queryset=ctype.model_class().objects.all(), widget=forms.TextInput)
            # for existing lessons, initialize the fields
            if kwargs.has_key('instance'):
                objects = ActivityRelation.objects.filter(activity=kwargs['instance'], content_type=ctype)
                if len(objects) > 0:
                    self.fields[field_name].initial = objects[0].object_id

    def clean(self):
        cleaned_data = super(ActivityForm, self).clean()
        for field in REQUIRED_FIELDS:
            field_name = field[0]
            app_label, model = field[1].split('.')

            if field_name not in self.cleaned_data:
                raise forms.ValidationError("%s is required." % field_name)
            elif self.cleaned_data[field_name].id != self.fields[field_name].initial:
                ar = ActivityRelation()
                # return an object of the model without saving to the DB
                ar.lesson = self.instance # self.save(commit=False)
                ar.content_type = ContentType.objects.get(app_label=app_label, model=model)
                ar.object_id = self.cleaned_data[field_name].id
                ar.content_object = self.cleaned_data[field_name]
                ar.save()
      # print self._errors
        return cleaned_data

class ContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = (JAVASCRIPT_URL + 'jquery-1.7.1.min.js',
              JAVASCRIPT_URL + 'genericcollections.js',
              JAVASCRIPT_URL + 'admin.js')

    def grade_levels(self, obj):
        return obj.grades.all().as_grade_range()

class ActivityAdmin(ContentAdmin):
    filter_horizontal = ['materials', 'physical_space_types', 'prior_activities', 'skills', 'tech_setup_types', 'tips']
    form = ActivityForm
    if RELATION_MODELS:
        inlines = [ConceptItemInline, VocabularyInline, ResourceInline, QuestionAnswerInline, InlineActivityRelation]
    else:
        inlines = [ConceptItemInline, VocabularyInline, ResourceInline, QuestionAnswerInline]
    list_display = ('title', 'description', 'pedagogical_purpose_type', 'grade_levels')
    list_filter = ('pedagogical_purpose_type',)
    search_fields = ['title', 'subtitle_guiding_question', 'description', 'id_number']

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('accessibility_notes', 'assessment', 'background_information', 'description', 'directions', 'learning_objectives', 'prior_knowledge', 'subtitle_guiding_question'):
            return db_field.formfield(widget=TinyMCE())
        return super(ActivityAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ('Overview',
                {'fields': [
                    'id_number', 'title', 'slug', 'pedagogical_purpose_type',
                    'description', 'subtitle_guiding_question',
                    'directions', 'duration', 'standards',
                    'notes_on_readability_score', 'is_modular', 'ads_excluded'
                 ],
                 'classes': ['collapse']}),
            ('Directions', {'fields': ['assessment_type', 'assessment', 'tips', 'extending_the_learning'], 'classes': ['collapse']}),
            ('Objectives', {'fields': ['learning_objectives', 'teaching_approach_type', 'teaching_method_types', 'skills'], 'classes': ['collapse']}),
            ('Preparation',
                {'fields': [
                    'materials', 'tech_setup_types', 'plugin_types',
                    'physical_space_types', 'setup', 'grouping_types',
                    'accessibility_notes', 'other_notes', 'prior_activities'
                 ],
                 'classes': ['collapse']}),
            ('Background & Vocabulary', {'fields': ['background_information', 'prior_knowledge'], 'classes': ['collapse']}),
            ('Credits, Sponsors, Partners', {'fields': ['credit'], 'classes': ['collapse']}),
            ('Global Metadata', {'fields': ['grades'], 'classes': ['collapse']}),
            ('Publishing', {'fields': ['published', 'published_date'], 'classes': ['collapse']}),
        ]
        for field in REQUIRED_FIELDS:
            fieldsets[0][1]['fields'].insert(4, field[0])
        return fieldsets

class ActivityInline(admin.TabularInline):
    model = LessonActivity
    raw_id_fields = ('activity',)

if RELATION_MODELS:
    class LessonFormSet(forms.models.BaseInlineFormSet):
        def get_queryset(self):
            'Returns all LessonRelation objects which point to our Lesson'
            return [x for x in super(LessonFormSet, self).get_queryset()
                if x.content_type.app_label + '.' + x.content_type.model in RELATION_MODELS]

    class InlineLessonRelation(GenericCollectionTabularInline):
        model = LessonRelation
        formset = LessonFormSet

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson

    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)
        for field in REQUIRED_FIELDS:
            field_name = field[0]
            app_label, model = field[1].split('.')
            ctype = ContentType.objects.get(app_label=app_label, model=model)
            self.fields[field_name] = forms.ModelChoiceField(queryset=ctype.model_class().objects.all(), widget=forms.TextInput)
            # for existing lessons, initialize the fields
            if kwargs.has_key('instance'):
                objects = LessonRelation.objects.filter(lesson=kwargs['instance'], content_type=ctype)
                if len(objects) > 0:
                    self.fields[field_name].initial = objects[0].object_id

    def clean(self):
        cleaned_data = super(LessonForm, self).clean()
        for field in REQUIRED_FIELDS:
            field_name = field[0]
            app_label, model = field[1].split('.')

            if field_name not in self.cleaned_data:
                raise forms.ValidationError("%s is required." % field_name)
            elif self.cleaned_data[field_name].id != self.fields[field_name].initial:
                lr = LessonRelation()
                # return an object of the model without saving to the DB
                lr.lesson = self.instance # self.save(commit=False)
                lr.content_type = ContentType.objects.get(app_label=app_label, model=model)
                lr.object_id = self.cleaned_data[field_name].id
                lr.content_object = self.cleaned_data[field_name]
                lr.save()
        return cleaned_data

class LessonAdmin(ContentAdmin):
    filter_horizontal = ['grades', 'materials', 'secondary_types', 'subjects']
    form = LessonForm
    if RELATION_MODELS:
        inlines = [ConceptItemInline, ActivityInline, InlineLessonRelation,]
    else:
        inlines = [ActivityInline,]
    list_display = ('title', 'description', 'appropriate_for', 'grade_levels')
    search_fields = ['title', 'description', 'id_number']

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('assessment', 'background_information', 'description', 'learning_objectives'):
            return db_field.formfield(widget=TinyMCE())
        return super(LessonAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ('Overview', {'fields': ['title', 'slug', 'subtitle_guiding_question', 'description', 'duration', 'id_number', 'is_modular', 'ads_excluded'], 'classes': ['collapse']}), # , 'create_date', 'last_updated_date'], 'classes': ['collapse']}),
            ('Directions', {'fields': ['assessment'], 'classes': ['collapse']}),
            ('Objectives', {'fields': ['learning_objectives'], 'classes': ['collapse']}),
            ('Preparation', {'fields': ['materials', 'other_notes'], 'classes': ['collapse']}),
            ('Background & Vocabulary', {'fields': ['background_information'], 'classes': ['collapse']}),
            ('Credits, Sponsors, Partners', {'fields': ['credit'], 'classes': ['collapse']}),
            ('Global Metadata', {'fields': ['secondary_types', 'subjects', 'grades'], 'classes': ['collapse']}),
            ('Content Related Metadata', {'fields': [], 'classes': ['collapse']}),
            ('Time and Date Metadata', {'fields': ['geologic_time'], 'classes': ['collapse']}),
            ('Publishing', {'fields': ['published', 'published_date'], 'classes': ['collapse']}),
        ]
        for field in REQUIRED_FIELDS:
            fieldsets[0][1]['fields'].insert(4, field[0])
        fieldsets[6][1]['fields'] = ['primary_category', 'secondary_categories']
        return fieldsets

class StandardAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('definition'):
            return db_field.formfield(widget=TinyMCE())
        return super(StandardAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class TipAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('body'):
            return db_field.formfield(widget=TinyMCE())
        return super(TipAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Activity, ActivityAdmin)
admin.site.register(GroupingType)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Material)
admin.site.register(Standard, StandardAdmin)
admin.site.register(TeachingMethodType)
admin.site.register(Tip, TipAdmin)
