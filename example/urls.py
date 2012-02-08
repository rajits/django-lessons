from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#    (r'^lessons/', include('lessons.urls')),
)

urlpatterns += patterns('',
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/(.*)', admin.site.root),
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
        'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
)
