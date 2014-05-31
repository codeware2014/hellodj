from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'hellodj.views.home'),
    url(r'^admin/', include(admin.site.urls)),
)
