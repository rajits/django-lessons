from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.utils.translation import ugettext, ugettext_lazy as _

from lessons.models import Activity, Lesson

def activity_detail(request, slug, template_name='lessons/activity_detail.html'):
	activity = get_object_or_404(Activity, slug=slug)

    return render_to_response(template_name, {
    	'activity': activity,
    }, context_instance=RequestContext(request))

def lesson_detail(request, slug, template_name='lessons/lesson_detail.html'):
	lesson = get_object_or_404(Lesson, slug=slug)

    return render_to_response(template_name, {
    	'lesson': lesson,
    }, context_instance=RequestContext(request))
