# import the standard Django Model
# from built-in library
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# declare a new model with a name "Musician"
class Musician(models.Model):
            # fields of the model
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    instrument_type = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

        # renames the instances of the model
        # with their first name
    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
