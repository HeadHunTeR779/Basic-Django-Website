#from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', { 'all_albums': all_albums })# note by default
                                                            # it thinks we r in templates folder

def detail(request, album_id):
    # album = Album.objects.get(pk = album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album' : album})

def favorite(request, album_id):
    album=get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html', { 'error_message': 'Invalid Request' })
    else:
        
        if (selected_song.is_favorite):
            selected_song.is_favorite = False
        else:
            selected_song.is_favorite = True

        selected_song.save()  #To echo to the data aboce line won't be saved IMPLICITLY!
        return render(request, 'music/details.html', {'album' : album})
