from django.db import models


class Song(models.Model):
    title= models.CharField(max_length= 255)
    artist= models.CharField(max_length= 255) 
    album= models.CharField(max_length= 255) 
    genre= models.CharField(max_length= 255)
    release_date= models.DateField(null=True)