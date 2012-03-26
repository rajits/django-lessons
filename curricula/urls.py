from django.conf.urls.defaults import *

urlpatterns = patterns('curricula.views',
    url(r'^activity/(?P<slug>[-\w]*)/$', 'activity_detail'),
    url(r'^lesson/(?P<slug>[-\w]*)/$', 'lesson_detail'),
    url(r'objectives/(?P<id>\d+)/$', 'learning_objectives'),
    url(r'^lesson/(?P<slug>[-\w]*)/materials/$', 'lesson_detail', {'template_name': 'curricula/fragments/materials.html'}),
    url(r'^lesson/(?P<slug>[-\w]*)/preparation/$', 'lesson_detail', {'template_name': 'curricula/fragments/preparation.html'}),
    url(r'background-information/(?P<id>\d+)/$', 'background_information'),
    url(r'get_breakout_terms/(?P<id>\d+)/$', 'get_breakout_terms'),
)
