from django.conf.urls.defaults import *

urlpatterns = patterns('views',
#   url(r'^$', 'views.index', name='index'),
    url(r'^activities/(?P<slug>.+)/$', 'activity_detail'),
    url(r'^lessons/(?P<slug>.+)/$'), 'lesson_detail'),
    url(r'^lessons/(?P<slug>.+)/assessments/$'), 'lesson_detail', {'template_name': 'lessons/fragments/assessments.html'}),
    url(r'^lessons/(?P<slug>.+)/learning-objectives/$'), 'lesson_detail', {'template_name': 'lessons/fragments/learning_objectives.html'}),
    url(r'^lessons/(?P<slug>.+)/background-information/$'), 'lesson_detail', {'template_name': 'lessons/fragments/background_information.html'}),
)
