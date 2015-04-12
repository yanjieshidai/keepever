from django.conf.urls import patterns, include, url
from django.contrib import admin
import evernote_dev.settings as settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'evernote_dev.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/', include('evernote_web.urls')),
    
)
