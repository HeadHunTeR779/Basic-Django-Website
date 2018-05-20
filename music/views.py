from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album



def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', { 'all_albums': all_albums })# note by default
                                                            # it thinks we r in templates folder

def detail(request, album_id):
    try:
        album = Album.objects.get(pk = album_id)
    except Album.DoesNotExist:
        raise Http404('Album Does Not Exist.')
    return render(request, 'music/details.html', {'album' : album})
