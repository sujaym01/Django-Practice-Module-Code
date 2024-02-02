# import form class from django
from django import forms

# import Album Model from models.py
from .models import Album

# create a ModelForm
class AlbumForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Album
		fields = "__all__"
