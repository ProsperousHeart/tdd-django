# from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    # url(
    #     r'^api/v1/puppies/(?P<pk>[0-9]+)$',
    #     views.get_delete_update_puppy,
    #     name='get_delete_update_puppy'
    # ),
    path(
        'api/v1/puppies/<int:pk>',
        views.get_delete_update_puppy,
        name='get_delete_update_puppy'
    ),
    
    # url(
    #     r'^api/v1/puppies/$',
    #     views.get_post_puppies,
    #     name='get_post_puppies'
    # )
    path(
        'api/v1/puppies/',
        views.get_post_puppies,
        name='get_post_puppies'
    )
]