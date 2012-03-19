from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db.models.loading import get_model
from django.utils.html import strip_tags

from genericcollection import GenericCollectionTabularInline

from models import *
from settings import (RELATION_MODELS, JAVASCRIPT_URL, ACTIVITY_FIELDS, 
                      LESSON_FIELDS, CREDIT_MODEL, REPORTING_MODEL)
from utils import truncate, ul_as_list
from widgets import ImportWidgetWrapper

from tinymce.widgets import TinyMCE
from audience.models import AUDIENCE_FLAGS
from audience.widgets import AdminBitFieldWidget, bitfield_display
from bitfield import BitField
from concepts.admin import ConceptItemInline

class VocabularyInline(admin.TabularInline):
    extra = 10
    model = Vocabulary
    raw_id_fields = ('glossary_term',)

class QuestionAnswerInline(admin.TabularInline):
    extra = 1
    formfield_overrides = {
        BitField: {
            'choices': AUDIENCE_FLAGS,
            'required': False,
            'widget': AdminBitFieldWidget()
        }
    }
    model = QuestionAnswer

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('question', 'answer'):
            return db_field.formfield(widget=TinyMCE(mce_attrs={'theme': "simple", 'width': 30, 'height': 5}))
        return super(QuestionAnswerInline, self).formfield_for_dbfield(db_field, **kwargs)

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
        for field in ACTIVITY_FIELDS:
            field_name = field[0]
            model = get_model(*field[1].split('.'))
            # ctype = ContentType.objects.get(app_label=app_label, model=model)
            self.fields[field_name] = forms.ModelChoiceField(queryset=model.objects.all(), widget=forms.TextInput)
            # for existing lessons, initialize the fields
            if kwargs.has_key('instance'):
                objects = kwargs['instance'].activityrelation_set.filter(relation_type=field_name)
                if len(objects) > 0:
                    self.fields[field_name].initial = objects[0].object_id

    def clean(self):
        cleaned_data = super(ActivityForm, self).clean()
        for field in ACTIVITY_FIELDS:
            field_name = field[0]
            app_label, model = field[1].split('.')

            if field_name not in self.cleaned_data:
                raise forms.ValidationError("%s is required." % field_name)
        return cleaned_data

class ContentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        BitField: {
            'choices': AUDIENCE_FLAGS,
            'initial': 1,
            'widget': AdminBitFieldWidget()
        }
    }
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        css = {'all': ('/media/static/audience/bitfield.css',)}
        js = ('/media/static/audience/bitfield.js',
              JAVASCRIPT_URL + 'jquery-1.7.1.min.js',
              JAVASCRIPT_URL + 'genericcollections.js',
              JAVASCRIPT_URL + 'admin.js')

    def get_title(self, obj):
        return strip_tags(obj.title)
    get_title.short_description = 'Title'

class ActivityAdmin(ContentAdmin):
    filter_horizontal = ['grades', 'grouping_types', 'materials', 'physical_space_types', 'prior_activities', 'skills', 'standards', 'subjects', 'teaching_method_types', 'tech_setup_types', 'tips', 'teaching_approaches', 'secondary_content_types']
    form = ActivityForm
    inlines = [ConceptItemInline, VocabularyInline, ResourceInline, QuestionAnswerInline]
    if RELATION_MODELS:
        inlines.append(InlineActivityRelation)

    list_display = ('get_title', 'description', 'pedagogical_purpose_type', 'grade_levels', 'published_date')
    list_filter = ('pedagogical_purpose_type',)
    if CREDIT_MODEL is not None:
        raw_id_fields = ("credit",)
    search_fields = ['title', 'subtitle_guiding_question', 'description', 'id_number']

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ('Overview',
                {'fields': [
                    'appropriate_for', 'title', 'slug',
                    'subtitle_guiding_question', 'description',
                    'pedagogical_purpose_type', 'duration', 'id_number',
                    'is_modular', 'ads_excluded', 'notes_on_readability_score'
                 ],
                 'classes': ['collapse']}),
            ('Directions', {'fields': ['directions', 'assessment_type', 'assessment', 'extending_the_learning', 'tips'], 'classes': ['collapse']}),
            ('Objectives', {'fields': ['learning_objectives', 'teaching_approaches', 'teaching_method_types', 'skills', 'standards'], 'classes': ['collapse']}),
            ('Preparation',
                {'fields': [
                    'setup', 'accessibility_notes', 'other_notes',
                    'grouping_types', 'materials', 'tech_setup_types',
                    'internet_access_type', 'plugin_types',
                    'physical_space_types'
                 ],
                 'classes': ['collapse']}),
            ('Background', {'fields': ['background_information', 'prior_knowledge', 'prior_activities'], 'classes': ['collapse']}),
            # ('Vocabulary', {'fields': [], 'classes': ['collapse']}),
        ]
        if CREDIT_MODEL is not None:
            fieldsets.append(('Credits, Sponsors, Partners', {'fields': ['credit'], 'classes': ['collapse']}))
        if REPORTING_MODEL is None:
            fieldsets.append(('Global Metadata', {'fields': ['secondary_content_types'], 'classes': ['collapse']}))
        else:
            fieldsets.append(('Global Metadata', {'fields': ['secondary_content_types', 'reporting_categories'], 'classes': ['collapse']}))
        fieldsets += [
            ('Content Related Metadata', {'fields': ['subjects', 'grades'], 'classes': ['collapse']}),
            ('Time and Date Metadata', {'fields': ['geologic_time', 'relevant_start_date', 'relevant_end_date'], 'classes': ['collapse']}),
            ('Publishing', {'fields': ['published', 'published_date'], 'classes': ['collapse']}),
        ]
        for field in ACTIVITY_FIELDS:
            fieldsets[0][1]['fields'].insert(4, field[0])
        return fieldsets

    def grade_levels(self, obj):
        return obj.grades.all().as_grade_range()
    
    def save_model(self, request, obj, form, change, *args, **kwargs):
        super(ActivityAdmin, self).save_model(request, obj, form, change, *args, **kwargs)
        
        for field, model in ACTIVITY_FIELDS:
            try:
                item = obj.activityrelation_set.get(relation_type=field)
                item.object_id = form[field].data
                item.save()
            except ActivityRelation.DoesNotExist:
                app_label, model = model.split('.')
                ctype = ContentType.objects.get(app_label=app_label, model=model)
                item = obj.activityrelation_set.create(relation_type=field, object_id=form[field].data, content_type_id=ctype.id)


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
  # background_information = forms.CharField(widget=ImportWidgetWrapper(forms.TextArea, 
  #             self.admin_site, obj_id=obj_id, field=db_field.name,
  #             object_name=self.object_name))
  # learning_objectives = forms.CharField(widget=ImportWidgetWrapper(forms.TextArea, 
  #             self.admin_site, obj_id=obj_id, field=db_field.name,
  #             object_name=self.object_name))

    class Meta:
        model = Lesson

    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)
        for field in LESSON_FIELDS:
            field_name = field[0]
            model = get_model(*field[1].split('.'))
            self.fields[field_name] = forms.ModelChoiceField(queryset=model.objects.all(), widget=forms.TextInput)
            # for existing lessons, initialize the fields
            if kwargs.has_key('instance'):
                objects = kwargs['instance'].lessonrelation_set.filter(relation_type=field_name)
                if len(objects) > 0:
                    self.fields[field_name].initial = objects[0].object_id

    def clean(self):
        cleaned_data = super(LessonForm, self).clean()
        for field in LESSON_FIELDS:
            field_name = field[0]
            app_label, model = field[1].split('.')

            if field_name not in self.cleaned_data:
                raise forms.ValidationError("%s is required." % field_name)
        return cleaned_data

class LessonAdmin(ContentAdmin):
    filter_horizontal = ['materials', 'secondary_content_types']
    form = LessonForm
    if RELATION_MODELS:
        inlines = [ConceptItemInline, ActivityInline, InlineLessonRelation,]
    else:
        inlines = [ActivityInline,]
    list_display = ('get_title', 'thumbnail_display', 'description', 'appropriate_display', 'published_date')
    list_filter = ('published_date',)
    if CREDIT_MODEL is not None:
        raw_id_fields = ("credit",)
    search_fields = ['title', 'description', 'id_number']

    def appropriate_display(self, obj):
        return bitfield_display(obj.appropriate_for)
    appropriate_display.short_description = 'Appropriate For'
    appropriate_display.allow_tags = True

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ('Overview', {'fields': ['appropriate_for', 'title', 'slug', 'subtitle_guiding_question', 'description', 'id_number', 'is_modular', 'ads_excluded'], 'classes': ['collapse']}), # , 'create_date', 'last_updated_date'], 'classes': ['collapse']}),
            ('Directions', {'fields': ['assessment'], 'classes': ['collapse']}),
            ('Objectives', {'fields': ['learning_objectives'], 'classes': ['collapse']}),
            ('Preparation', {'fields': ['materials', 'other_notes'], 'classes': ['collapse']}),
            ('Background & Vocabulary', {'fields': ['background_information'], 'classes': ['collapse']}),
        ]
        if CREDIT_MODEL is not None:
            fieldsets.append(('Credits, Sponsors, Partners', {'fields': ['credit'], 'classes': ['collapse']}))
        if REPORTING_MODEL is None:
            fieldsets.append(('Global Metadata', {'fields': ['secondary_content_types'], 'classes': ['collapse']}))
        else:
            fieldsets.append(('Global Metadata', {'fields': ['secondary_content_types', 'reporting_categories'], 'classes': ['collapse']}))
        fieldsets += [
            ('Time and Date Metadata', {'fields': ['geologic_time', 'relevant_start_date', 'relevant_end_date'], 'classes': ['collapse']}),
            ('Publishing', {'fields': ['published', 'published_date'], 'classes': ['collapse']}),
        ]
        for field in LESSON_FIELDS:
            fieldsets[0][1]['fields'].insert(4, field[0])
        return fieldsets

    def save_model(self, request, obj, form, change, *args, **kwargs):
        super(LessonAdmin, self).save_model(request, obj, form, change, *args, **kwargs)

        for field, model in LESSON_FIELDS:
            try:
                item = obj.lessonrelation_set.get(relation_type=field)
                item.object_id = form[field].data
                item.save()
            except LessonRelation.DoesNotExist:
                app_label, model = model.split('.')
                ctype = ContentType.objects.get(app_label=app_label, model=model)
                item = obj.lessonrelation_set.create(relation_type=field, object_id=form[field].data, content_type_id=ctype.id)

    def thumbnail_display(self, obj):
        ctype = ContentType.objects.get(app_label='core_media', model='ngphoto')
        lr = LessonRelation.objects.filter(lesson=obj, content_type=ctype)
        if len(lr) > 0:
            return '<img src="%s"/>' % lr[0].content_object.thumbnail_url()
        else:
            return None
    thumbnail_display.allow_tags = True

class TypeAdmin(admin.ModelAdmin):
    search_fields = ['name']

class AppropriateAdmin(admin.ModelAdmin):
    formfield_overrides = {
        BitField: {
            'choices': AUDIENCE_FLAGS,
            'widget': AdminBitFieldWidget()
        }
    }

    class Media:
        css = {'all': ('/media/static/audience/bitfield.css',)}
        js = ('/media/static/audience/bitfield.js',
              JAVASCRIPT_URL + 'jquery-1.7.1.min.js')

class StandardAdmin(AppropriateAdmin):
    filter_horizontal = ['grades']
    list_display = ('standard_type', 'name', 'grade_levels')
    list_filter = ('standard_type', 'state', 'grades')
    search_fields = ['name', 'definition']

    def grade_levels(self, obj):
        return obj.grades.all().as_grade_range()
    grade_levels.short_description = 'Grades'

class TipAdmin(AppropriateAdmin):
    list_display = ('body_display', 'tip_type', 'appropriate_display')
    list_filter = ('tip_type',)
    search_fields = ['body', 'id_number']

    def appropriate_display(self, obj):
        return bitfield_display(obj.appropriate_for)
    appropriate_display.short_description = 'Appropriate For'
    appropriate_display.allow_tags = True

    def body_display(self, obj):
        return truncate(strip_tags(obj.body), 90)
    body_display.short_description = 'Body'

admin.site.register(Activity, ActivityAdmin)
admin.site.register(GroupingType)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Material, TypeAdmin)
admin.site.register(Standard, StandardAdmin)
admin.site.register(TeachingMethodType, TypeAdmin)
admin.site.register(Tip, TipAdmin)
