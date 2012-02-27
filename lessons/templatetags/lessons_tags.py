from django import template
from django.conf import settings

register = template.Library()

tabs = (
    ('Overview', 'Directions', 'Objectives', 'Background'),
    ('Global Metadata', 'Content Related Metadata', 'Time and Date Metadata'),
)

@register.filter(name='tab_num')
def tab_num(fieldset):
    for count, fieldsets in enumerate(tabs):
        if fieldset.name in fieldsets:
            return count
    return 0

@register.filter(name='get_model')
def get_model(field):
    for name, model in settings.LESSON_SETTINGS['REQUIRED_FIELDS']:
        if field == name:
            return model
    return None
