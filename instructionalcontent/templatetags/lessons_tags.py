from django import template
from instructionalcontent.settings import ACTIVITY_FIELDS, LESSON_FIELDS

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
    return get_model(field, ACTIVITY_FIELDS)

@register.filter(name='get_lesson_model')
def get_lesson_model(field):
    return get_model(field, LESSON_FIELDS)

@register.filter(name='lesson_slug')
def lesson_slug(id):
    from instructionalcontent.models import Lesson

    return Lesson.objects.get(id=id).slug

@register.filter(name='activity_slug')
def activity_slug(id):
    from instructionalcontent.models import Activity

    return Activity.objects.get(id=id).slug
