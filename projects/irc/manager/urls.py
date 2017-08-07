from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as authviews
from manager import views

urlpatterns = [
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    url(r'^createUser/$', views.create_user),
    url(r'^channels/$', views.channel_list),
    url(r'^channels/(?P<pk>[0-9]+)/$', views.channel_detail),
    url(r'^channels/(?P<pk>[0-9]+)/posts/$', views.post_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
