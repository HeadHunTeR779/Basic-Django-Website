from django.conf.urls import url
from . import views

urlpatterns = [

    # /music/
    url(r'^$', views.index, name='index'),    #notice no () in function call

    # /music/762/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),            #notice no () in function call
]
