from django.conf.urls import patterns, include, url
from django.contrib import admin

#Hi it's Mente, adding a line

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
