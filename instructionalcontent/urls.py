from django.conf.urls.defaults import *

urlpatterns = patterns('instructionalcontent.views',
    url(r'^activity/(?P<slug>[-\w]*)/$', 'activity_detail'),
    url(r'^lesson/(?P<slug>[-\w]*)/$', 'lesson_detail'),
    url(r'^lesson/(?P<slug>[-\w]*)/objectives/$', 'lesson_detail', {'template_name': 'instructionalcontent/fragments/objectives.html'}),
    url(r'^lesson/(?P<slug>[-\w]*)/materials/$', 'lesson_detail', {'template_name': 'instructionalcontent/fragments/materials.html'}),
    url(r'^lesson/(?P<slug>[-\w]*)/preparation/$', 'lesson_detail', {'template_name': 'instructionalcontent/fragments/preparation.html'}),
    url(r'^lesson/(?P<slug>[-\w]*)/background-information/$', 'lesson_detail', {'template_name': 'instructionalcontent/fragments/bg_info.html'}),
)
