from django.conf.urls import url

from puppies.views import get_delete_update_puppy, get_post_puppies

urlpatterns = [
    url(r'^api/v1/puppies/(?P<pk>[0-9]+)$', get_delete_update_puppy, name='get_delete_update_puppy'),
    url(r'^api/v1/puppies/$', get_post_puppies, name='get_post_puppies'),
]
