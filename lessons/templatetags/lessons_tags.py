from django import template

register = template.Library()

@register.filter(name='active_tab')
def active_tab(request):
    full_path = request.get_full_path()
    search_str = 'active_tab='
    start = full_path.find(search_str)
    if start > -1:
        return full_path[start+len(search_str):]
    else:
        return '1'

@register.filter(name='display_in_tab')
def display_in_tab(fieldset, request):
    tabs = [
        ('Overview', 'Directions', 'Objectives', 'Background'),
        ('Global Metadata', 'Time and Date Metadata'),
    ]
    tab = active_tab(request)
    index = int(tab) - 1 # list is zero-based
    return fieldset.name in tabs[index]
