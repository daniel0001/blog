from django.conf.urls import url
from blog.views import *


urlpatterns = [
    url(r'^$', post_list, name="post_list"),
    url(r'^(?P<id>\d+)/$', post_detail, name="post_detail"),
    url(r'^post/new/$', new_post, name='new_post'),
    url(r'^(?P<id>\d+)/edit$', edit_post, name='edit')
]
