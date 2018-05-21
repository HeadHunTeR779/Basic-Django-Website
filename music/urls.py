from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [

    # /music/      === he is catching nothing
    url(r'^$', views.index, name='index'),    #notice no () in function call

    # /music/album_id/    == he is saying anything of the REGULAR EXPRESSION TYPE i.e. a nos after music/
                        #and the number is saved in albun_id variable
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),  #notice no () in function call
]
