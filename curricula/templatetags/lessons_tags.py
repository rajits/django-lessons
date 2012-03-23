from django import template

from curricula.models import Activity, Lesson
from curricula.settings import KEY_IMAGE, RESOURCE_CAROUSEL, RC_SLIDE

register = template.Library()

tabs = (
    ('Overview', 'Directions', 'Objectives', 'Background & Vocabulary', 'Credits, Sponsors, Partners'),
    ('Global Metadata', 'Content Related Metadata', 'Time and Date Metadata', 'Publishing'),
)

@register.filter(name='tab_num')
def tab_num(fieldset):
    for count, fieldsets in enumerate(tabs):
        if fieldset.name in fieldsets:
            return count
    return 0

def get_model(field, setting):
    for name, model in setting:
        if field == name:
            return model
    return None

@register.filter(name='get_activity_model')
def get_activity_model(field):
    return get_model(field, (KEY_IMAGE, RESOURCE_CAROUSEL))

@register.filter(name='get_lesson_model')
def get_lesson_model(field):
    return get_model(field, (KEY_IMAGE, RC_SLIDE))

@register.filter(name='lesson_slug')
def lesson_slug(id):
    if id:
        return Lesson.objects.get(id=id).slug
    else:
        return None

@register.filter(name='activity_slug')
def activity_slug(id):
    if id:
        return Activity.objects.get(id=id).slug
    else:
        return None

@register.filter(name='activity_thumbnail')
def activity_thumbnail(id):
    try:
        return Activity.objects.get(id=id).thumbnail_html()
    except Activity.DoesNotExist:
        return None

@register.filter(name='lesson_thumbnail')
def lesson_thumbnail(id):
    try:
        return Lesson.objects.get(id=id).thumbnail_html()
    except Lessons.DoesNotExist:
        return None
