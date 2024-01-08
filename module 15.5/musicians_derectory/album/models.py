# import the standard Django Model
# from built-in library
from django.db import models
from musician.models import Musician
# Create your models here.

# specifying choices  
RATING_CHOICES = ( 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"), 
)
# declare a new model with a name "Album" 
class Album(models.Model):
        # fields of the model
    album_name = models.CharField(max_length= 50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_release_date = models.DateTimeField(auto_now_add=True)
    # album_release_date = models.DateField(auto_now_add=True)
    album_rating = models.CharField(
        max_length= 20,
        choices = RATING_CHOICES,
        default = '1',
        )
    
        # renames the instances of the model
        # with their album_name name
    def __str__(self):
        return self.album_name 
        


