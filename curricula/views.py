from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.utils.translation import ugettext, ugettext_lazy as _

from settings import RELATION_MODELS, LESSON_FIELDS
from curricula.models import Activity, Lesson

def activity_detail(request, slug, template_name='lessons/activity_detail.html'):
    activity = get_object_or_404(Activity, slug=slug)

    return render_to_response(template_name, {
        'activity': activity,
    }, context_instance=RequestContext(request))

def lesson_detail(request, slug, template_name='lessons/lesson_detail.html'):
    lesson = get_object_or_404(Lesson, slug=slug)

    getvars = request.GET.copy()
    if getvars.has_key('activities'):
        activities = getvars['activities']
    else:
        activities = lesson.get_activities()

    context = {
        'lesson': lesson,
        'activities': activities,
    }

    for field in LESSON_FIELDS:
        related_ctypes = lesson.get_related_content_type(field[0])
        if len(related_ctypes) > 0:
            context[field[0]] = related_ctypes[0].content_object

    for model in RELATION_MODELS:
        name = model.split('.')[1]
        related_ctypes = lesson.get_related_content_type(name)
        if len(related_ctypes) > 0:
            context[name] = related_ctypes[0].content_object

    return render_to_response(template_name, context, context_instance=RequestContext(request))

def background_information(request, id):
    lesson = get_object_or_404(Lesson, id=id)
    background_information = ''

    for activity in lesson.get_activities():
        background_information += activity.background_information

    context = { 'background_information': background_information, }
    return render_to_response('lessons/background_information.html',
                              context,
                              context_instance=RequestContext(request))

def learning_objectives(request, id):
    lesson = get_object_or_404(Lesson, id=id)
    learning_objectives = []

    for activity in lesson.get_activities():
        learning_objectives += ul_as_list(activity.learning_objectives)
    deduped_objectives = set(learning_objectives)

    context = { 'learning_objectives': list(learning_objectives), }
    return render_to_response('lessons/learning_objectives.html',
                              context,
                              context_instance=RequestContext(request))
