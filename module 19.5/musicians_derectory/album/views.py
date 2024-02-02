from django.shortcuts import render, redirect
from . import forms
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView,DeleteView
# Create your views here.
@login_required
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


# Add album using class based view
@method_decorator(login_required, name='dispatch')
class AddAlbumCreateView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



@login_required
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


# album edit using class based view
@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    


@login_required
def delete_album(request,id):
    album = models.Album.objects.get(pk=id).delete()
    # album.delete()
    return redirect('homepage')


# album delete using class based view
@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete_album.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

