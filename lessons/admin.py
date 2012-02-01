from django.contrib import admin
from models import *

class ActivityAdmin(admin.ModelAdmin):
    filter_horizontal = ['materials', 'physical_space_types', 'skills', 'tech_setup_types', 'tips']
    prepopulated_fields = {"slug": ("title",)}

class ActivityInline(admin.TabularInline):
    model = LessonActivity

class LessonAdmin(admin.ModelAdmin):
    filter_horizontal = ['materials',]
    inlines = [
        ActivityInline,
    ]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Material)
