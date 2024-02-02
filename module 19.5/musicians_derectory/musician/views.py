from django.shortcuts import render, redirect
from . import forms
from . import models
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView


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


# Add music using class based view
@method_decorator(login_required, name='dispatch')
class AddMusicCreateView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_music.html'
    success_url = reverse_lazy('add_music')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




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


# music edit using class based view
@method_decorator(login_required, name='dispatch')
class EditMusicView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_music.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    