from django.contrib import admin
from models import Activity, Lesson, LessonActivity, Material, Tip

class ActivityAdmin(admin.ModelAdmin):
    fields = ['slug', 'id_number', 'title', 'pedagogical_purpose_type', 'description', 'subtitle_guiding_question', 'learning_objectives', 'background_information', 'prior_knowledge', 'setup', 'accessibility_notes', 'directions', 'assessment_type', 'duration_minutes', 'teaching_approach_type', 'teaching_method_type', 'grouping_type', 'tech_setup_types', 'plugin_types', 'tips', 'skills', 'materials', 'physical_space_types']
    filter_horizontal = ['materials', 'physical_space_types', 'skills', 'tech_setup_types', 'tips']
    prepopulated_fields = {"slug": ("title",)}

class ActivityInline(admin.TabularInline):
    model = LessonActivity

class LessonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Overview', {'fields': ['create_date', 'last_updated_date', 'title', 'slug', 'subtitle_guiding_question', 'description', 'duration_in_minutes', 'id_number', 'is_modular', 'ads_excluded', 'materials', 'physical_space_type'], 'classes': ['collapse']}),
        ('Directions', {'fields': ['assessment'], 'classes': ['collapse']}),
        ('Objectives', {'fields': ['learning_objectives'], 'classes': ['collapse']}),
        ('Background', {'fields': ['background_information'], 'classes': ['collapse']}),
    ]
    filter_horizontal = ['materials',]
    inlines = [
        ActivityInline,
    ]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Material)
admin.site.register(Tip)
