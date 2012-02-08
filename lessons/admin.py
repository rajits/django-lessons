from django.contrib import admin
from django.core.urlresolvers import reverse

from models import Activity, Lesson, LessonActivity, Material, Standard, Tip

from tinymce.widgets import TinyMCE

class ActivityAdmin(admin.ModelAdmin):
    fields = ['slug', 'id_number', 'title', 'pedagogical_purpose_type', 'description', 'subtitle_guiding_question', 'learning_objectives', 'background_information', 'prior_knowledge', 'setup', 'accessibility_notes', 'directions', 'assessment_type', 'duration_minutes', 'teaching_approach_type', 'teaching_method_type', 'grouping_type', 'tech_setup_types', 'plugin_types', 'tips', 'skills', 'materials', 'physical_space_types']
    filter_horizontal = ['materials', 'physical_space_types', 'skills', 'tech_setup_types', 'tips']
    prepopulated_fields = {"slug": ("title",)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('accessibility_notes', 'background_information', 'description', 'directions', 'learning_objectives', 'prior_knowledge', 'subtitle_guiding_question'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(ActivityAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class ActivityInline(admin.TabularInline):
    model = LessonActivity

class LessonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Overview', {'fields': ['title', 'slug', 'subtitle_guiding_question', 'description', 'duration_in_minutes', 'id_number', 'is_modular', 'ads_excluded', 'materials', 'physical_space_type'], 'classes': ['collapse']}), # , 'create_date', 'last_updated_date'], 'classes': ['collapse']}),
        ('Directions', {'fields': ['assessment'], 'classes': ['collapse']}),
        ('Objectives', {'fields': ['learning_objectives'], 'classes': ['collapse']}),
        ('Background', {'fields': ['background_information'], 'classes': ['collapse']}),
    ]
    filter_horizontal = ['materials',]
    inlines = [
        ActivityInline,
    ]
    prepopulated_fields = {"slug": ("title",)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('assessment', 'background_information', 'description', 'learning_objectives'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(LessonAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class TipAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('body'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
            ))
        return super(TipAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Material)
admin.site.register(Standard)
admin.site.register(Tip, TipAdmin)
