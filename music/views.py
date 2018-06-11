from django.views import generic
from .models import Album
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth import authenticate, login   #authenticate makes sure whether given pass and id is in databse or not
                #login just gives them a session so that they dont have to authenticate again and again. means it keep the user "logged in"

from django.shortcuts import render, redirect #redirect, redirects the user to a given page after login
#render  to transform the template and provided variables for presentation to a user.

from .forms import UserForm

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

class UserFormView(generic.View):
    model=UserForm
    template_name = 'music/registration-form.html'

    def get(self, request):         #When user opened the page and wants the empty form
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})               #just making the template and variables to be presented to the user



    # this is when user filled the form, now we process data,add them to the database, log them in, redirect them
    def post(self, :request):       #get() and post() are basically instances of same page.
        form = self.form_class(request.POST)

        if form.is_valid():  #cleaned_data won't work wihout first calling this it validates every attribute email etc
            user = form.save(commit=False)

            #clean (normalize the data its just been validated by is_valid)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)       #special way for passwords because they are encrypted
            user.save()
