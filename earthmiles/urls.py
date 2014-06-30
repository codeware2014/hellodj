__author__ = 'Som'

from django.conf.urls import patterns, url,include
from rest_framework.urlpatterns import format_suffix_patterns
from earthmiles import views

urlpatterns = patterns('',
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(),name='snippet-detail'),

    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'users/(?P<pk>[0-9]+)/$', views.UserDetails.as_view(), name='user-detail'),
    url(r'^$', 'earthmiles.views.api_root'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(),name='snippet-highlight'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), #for login and logout
)

urlpatterns = format_suffix_patterns(urlpatterns)
#this is for switching between json and api