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

@register.filter(name='is_required')
def is_required(field):
	for name, model in settings.LESSON_SETTINGS['REQUIRED_FIELDS']:
		if field == name:
			return True
	return False

@register.filter(name='content_types')
def content_types(field):
	return None
