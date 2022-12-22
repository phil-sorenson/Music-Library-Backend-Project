from django.contrib import admin
from .models import Song

#! In order to use the Admin site (That we got through creating the superuser) we must import our models/Song model👆 & register our Song model in 'admin.py' 👇
admin.site.register(Song)