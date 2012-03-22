from django.conf.urls.defaults import *

urlpatterns = patterns('curricula.views',
    url(r'^activity/(?P<slug>[-\w]*)/$', 'activity_detail'),
    url(r'^lesson/(?P<slug>[-\w]*)/$', 'lesson_detail'),
    url(r'^lesson/(?P<slug>[-\w]*)/objectives/$', 'lesson_detail', {'template_name': 'curricula/fragments/objectives.html'}),
    url(r'^lesson/(?P<slug>[-\w]*)/materials/$', 'lesson_detail', {'template_name': 'curricula/fragments/materials.html'}),
    url(r'^lesson/(?P<slug>[-\w]*)/preparation/$', 'lesson_detail', {'template_name': 'curricula/fragments/preparation.html'}),
    url(r'^lesson/(?P<slug>[-\w]*)/background-information/$', 'lesson_detail', {'template_name': 'curricula/fragments/bg_info.html'}),
)
