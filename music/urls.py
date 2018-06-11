from django.conf.urls import url
from . import views

#EVERY VIEW MUST HAVE A URL!!!!!!!!!!!!!!!!!!!!!!!

app_name = 'music'

urlpatterns = [

    # /music/      === he is catching nothing
    url(r'^$', views.IndexView.as_view(), name='index'),    #notice no () in function call

    # /music/album_id/    == he is saying anything of the REGULAR EXPRESSION TYPE i.e. a nos after music/
                        #and the number is saved in albun_id variable
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),  #notice no () in function call

    # /music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/update/2    2 is like the pk or you may say the id
    url(r'album/update/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    #/music/album/delete/2  2 is again like i said the primary key [pk]
    url(r'album/delete/(?P<pk>[0-9]+)/$', views.AlbumDelete.as_view(), name='album-delete'),

    url(r'register/$', views.UserFormView.as_view(), name='register'),

]
