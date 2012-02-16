from django import template

register = template.Library()

tabs = (
    ('Overview', 'Directions', 'Objectives', 'Background'),
    ('Global Metadata', 'Time and Date Metadata'),
)

@register.filter(name='tab_num')
def tab_num(fieldset):
    for count, fieldsets in enumerate(tabs):
        if fieldset.name in fieldsets:
            return count
    return 0
