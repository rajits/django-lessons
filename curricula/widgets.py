import copy

from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

class WidgetWrapper(forms.Widget):
    """
    Handles all the other methods that you aren't going to override but are
    necessary for the original widget to work.
    """
    def __init__(self, widget, *args, **kwargs):
        self.widget = widget
    
    def __deepcopy__(self, memo):
        obj = copy.copy(self)
        obj.widget = copy.deepcopy(self.widget, memo)
        obj.attrs = self.widget.attrs
        memo[id(self)] = obj
        return obj
    
    def _media(self):
        return self.widget.media
    media = property(_media)
    
    def build_attrs(self, extra_attrs=None, **kwargs):
        "Helper function for building an attribute dictionary."
        self.attrs = self.widget.build_attrs(extra_attrs, **kwargs)
        return self.attrs

    def value_from_datadict(self, data, files, name):
        return self.widget.value_from_datadict(data, files, name)

    def _has_changed(self, initial, data):
        return self.widget._has_changed(initial, data)

    def id_for_label(self, id_):
        return self.widget.id_for_label(id_)
    
    def render(self, name, value, *args, **kwargs):
        return self.widget.render(name, value, *args, **kwargs)


class ImportWidgetWrapper(WidgetWrapper):
    """
    Wrap a widget and add the link buttons at the end
    """
    def __init__(self, widget): # , admin_site, obj_id, field, object_name):
        self.widget = widget
      # self.admin_site = admin_site
      # self.obj_id = obj_id
      # self.field = field
      # self.app_label = "curricula"
      # self.object_name = object_name
        super(ImportWidgetWrapper, self).__init__(widget)

    def render(self, name, value, *args, **kwargs):
        output = [self.widget.render(name, value, *args, **kwargs)]

        output.append(u'<div style="display:inline-block;padding-left:10px">')
        output.append(u'<a href="" class="import-text" id="add_id_%s"> ' # onclick="return showAddAnotherPopup(this);"> '
                      % name)
        output.append(u'&nbsp;%s</a>&nbsp;<br>' % _('Import Text from Activities'))
        output.append(u'</div>')

        return mark_safe(u''.join(output))
