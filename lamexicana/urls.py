from django.conf.urls.defaults import *
from website.views import *
from signs.views import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

js_info_dict = {
    'packages': ('media.js',),
}

urlpatterns = patterns('',
    (r'^404/$', error404),
    (r'^500/$', error500),
    (r'^admin/', include(admin.site.urls)),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog',js_info_dict),
    (r'^medios/(?P<path>.*)$', 'django.views.static.serve',{
                    'document_root' : settings.MEDIA_ROOT,
                    'show_indexes':True
    }),
    (r'^$', index),
    (r'^new/$', new),
)
