# import form class from django
from django import forms

# import  Musician  Model from models.py
from .models import Musician

# create a ModelForm
class MusicianForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Musician
		fields = "__all__"
