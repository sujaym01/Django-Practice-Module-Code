from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def add_music(request):
    if request.method == 'POST':
        # create object of form
        musician_form = forms.MusicianForm(request.POST)
        # check if form data is valid
        if musician_form.is_valid():
            # save the form data to model
            musician_form.save()
            # show data add_music.html page
            return redirect('add_music')
    
    else:
        # user get a blank form when visiting the website
        musician_form = forms.MusicianForm()
    return render(request, 'add_music.html', {'form' : musician_form})



def edit_music(request,id):
    music = models.Musician.get(pk=id)
    # Create object of form and add it to the instance of Musician class because
    # we want to edit  MusicianForm that's will fillup this fields.
    musician_form = forms.MusicianForm(instance=music)
    print(music.name)
    if request.method == 'POST':
        # Create object of form and add it to the instance of Musician class beacuse
        # we don't want to Submit a new MusicianForm
        musician_form = forms.MusicianForm(request.POST,instance=music)
        # check if form data is valid
        if musician_form.is_valid():
            # save the form data to model
            musician_form.save()
            # show data add_music.html page
            return redirect('homepage')
    return render(request, 'add_music.html', {'form' : musician_form})