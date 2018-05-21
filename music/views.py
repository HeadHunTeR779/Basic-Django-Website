from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album



def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', { 'all_albums': all_albums })# note by default
                                                            # it thinks we r in templates folder

def detail(request, album_id):
    # album = Album.objects.get(pk = album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album' : album})
