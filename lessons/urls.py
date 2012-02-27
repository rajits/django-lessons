from django.conf.urls.defaults import *

urlpatterns = patterns('lessons.views',
    url(r'^activity/(?P<slug>[-\w]*)/$', 'activity_detail'),
    url(r'^lesson/(?P<slug>[-\w]*)/$', 'lesson_detail'),
    url(r'^lesson/(?P<slug>[-\w]*)/objectives/$', 'lesson_detail', {'template_name': 'lessons/fragments/objectives.html'}),
    url(r'^lesson/(?P<slug>[-\w]*)/materials/$', 'lesson_detail', {'lessons/fragments/materials.html'}),
    url(r'^lesson/(?P<slug>[-\w]*)/preparation/$', 'lesson_detail', {'template_name': 'lessons/fragments/preparation.html'}),
    url(r'^lesson/(?P<slug>[-\w]*)/background-information/$', 'lesson_detail', {'template_name': 'lessons/fragments/bg_info.html'}),
)
