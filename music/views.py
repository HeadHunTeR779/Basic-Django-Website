from django.views import generic
from .models import Album
from django.core.urlresolvers import reverse_lazy

#EVERY VIEW MUST HAVE A URL!!!!

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album  #What do you wanna display?
    template_name = 'music/details.html'  #Where's the template relative to the folder named templates.

class AlbumCreate(generic.edit.CreateView): #see album_form for input form
    model = Album  #What do you wanna create?
    fields = ['artist', 'album_title', 'genre', 'album_logo']  #What fields you wanna fill up? Like Youtube may ask you to fill up Video
    #description tags and stuff but won't ask about Comments or views or likes although they are probably the fields of their video class.

class AlbumUpdate(generic.edit.UpdateView):
    model = Album  #What do you wanna update?
    fields=['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(generic.edit.DeleteView):
    model = Album  #What do you wanna delete?
    success_url = reverse_lazy('music:index')
