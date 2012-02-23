from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from genericcollection import GenericCollectionTabularInline

from models import *
from settings import RELATION_MODELS, JAVASCRIPT_URL, REQUIRED_FIELDS

from tinymce.widgets import TinyMCE

class ActivityAdmin(admin.ModelAdmin):
    fields = ['slug', 'id_number', 'title', 'pedagogical_purpose_type', 'description', 'subtitle_guiding_question', 'learning_objectives', 'background_information', 'prior_knowledge', 'setup', 'accessibility_notes', 'other_notes', 'directions', 'assessment_type', 'assessment', 'duration', 'grades', 'teaching_approach_type', 'teaching_method_types', 'grouping_types', 'tech_setup_types', 'plugin_types', 'tips', 'skills', 'materials', 'physical_space_types', 'standards']
    filter_horizontal = ['materials', 'physical_space_types', 'skills', 'tech_setup_types', 'tips']
    prepopulated_fields = {"slug": ("title",)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('accessibility_notes', 'assessment', 'background_information', 'description', 'directions', 'learning_objectives', 'prior_knowledge', 'subtitle_guiding_question'):
            return db_field.formfield(widget=TinyMCE())
        return super(ActivityAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class ActivityInline(admin.TabularInline):
    model = LessonActivity

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
            self.fields[field_name] = forms.ModelChoiceField(queryset=ctype.model_class().objects.all(), widget=forms.TextInput) # admin.widgets.ForeignKeyRawIdWidget(LessonRelation._meta.get_field('content_type').rel))
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

            if self.cleaned_data[field_name].id != self.fields[field_name].initial:
                lr = LessonRelation()
                # return an object of the model without saving to the DB
                lr.lesson = self.instance # self.save(commit=False)
                lr.content_type = ContentType.objects.get(app_label=app_label, model=model)
                lr.object_id = self.cleaned_data[field_name].id
                lr.content_object = self.cleaned_data[field_name]
                lr.save()
        return cleaned_data

class LessonAdmin(admin.ModelAdmin):
    filter_horizontal = ['grades', 'materials', 'secondary_types', 'subjects']
    form = LessonForm
    if RELATION_MODELS:
        inlines = [ActivityInline, InlineLessonRelation,]
    else:
        inlines = [ActivityInline,]
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = (JAVASCRIPT_URL + 'jquery-1.7.1.min.js',
              JAVASCRIPT_URL + 'genericcollections.js',
              JAVASCRIPT_URL + 'init-inlines.js')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('assessment', 'background_information', 'description', 'learning_objectives'):
            return db_field.formfield(widget=TinyMCE())
        return super(LessonAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ('Overview', {'fields': ['title', 'slug', 'subtitle_guiding_question', 'description', 'duration', 'id_number', 'is_modular', 'ads_excluded', 'materials', 'physical_space_type'], 'classes': ['collapse']}), # , 'create_date', 'last_updated_date'], 'classes': ['collapse']}),
            ('Directions', {'fields': ['assessment'], 'classes': ['collapse']}),
            ('Objectives', {'fields': ['learning_objectives'], 'classes': ['collapse']}),
            ('Background', {'fields': ['background_information'], 'classes': ['collapse']}),
            ('Global Metadata', {'fields': ['secondary_types', 'subjects', 'grades'], 'classes': ['collapse']}),
            ('Content Related Metadata', {'fields': [], 'classes': ['collapse']}),
            ('Time and Date Metadata', {'fields': ['geologic_time'], 'classes': ['collapse']}),
        ]
        for field in REQUIRED_FIELDS:
            fieldsets[0][1]['fields'].insert(4, field[0])
        fieldsets[5][1]['fields'] = ['primary_category', 'secondary_categories']
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
