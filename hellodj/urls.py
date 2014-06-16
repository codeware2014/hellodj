from django.conf.urls import patterns, include, url

from django.contrib import admin


from earthmiles import views

from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover()

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'hellodj.views.home'),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include(router.urls)),    #this one makes the home page a testing ground for the rest apis
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # url(r'^snippet/$',views.SnippetList.as_view()),
    # url(r'^snippet/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)






