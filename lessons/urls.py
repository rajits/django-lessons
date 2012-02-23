from django.conf.urls.defaults import *

urlpatterns = patterns('lessons.views',
    url(r'^activity/(?P<slug>[-\w]*)/$', 'activity_detail'),
    url(r'^lesson/(?P<slug>[-\w]*)/$', 'lesson_detail'),
    url(r'^lesson/(?P<slug>[-\w]*)/subjects/$', 'lesson_detail', {'template_name': 'lessons/fragments/subjects.html'}),
    url(r'^lesson/(?P<slug>[-\w]*)/learning-objectives/$', 'lesson_detail', {'template_name': 'lessons/fragments/learning_objectives.html'}),
    url(r'^lesson/(?P<slug>[-\w]*)/other-notes/$', 'lesson_detail', {'template_name': 'lessons/fragments/other_notes.html'}),
    url(r'^lesson/(?P<slug>[-\w]*)/background-information/$', 'lesson_detail', {'template_name': 'lessons/fragments/bg_info.html'}),
)
