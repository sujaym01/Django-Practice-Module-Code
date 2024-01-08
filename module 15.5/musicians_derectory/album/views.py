from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def add_album(request):
    if request.method == 'POST':
        # create object of form
        album_form = forms.AlbumForm(request.POST)
        # check if form data is valid
        if album_form.is_valid():
            # save the form data to model
            album_form.save()
            # show data ad_album.html page
            return redirect('add_album')
    
    else:
        # user get a blank form when visiting the website
        album_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form' : album_form})


def edit_album(request,id):
    album = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    # print(album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    return render(request, 'add_album.html', {'form' : album_form})

def delete_album(request,id):
    album = models.Album.objects.get(pk=id).delete()
    # album.delete()
    return redirect('homepage')
