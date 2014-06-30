from django.conf.urls import patterns, include, url

from django.contrib import admin

from rest_framework import routers
from earthmiles import views

admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'hellodj.views.home'),
    url(r'^admin/', include(admin.site.urls)),




    url(r'^', include('earthmiles.urls')),

)






