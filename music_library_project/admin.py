from django.contrib import admin
from .models import Song

#! In order to use the Admin site (That we got through creating the superuser) we must import our models/Song model๐ & register our Song model in 'admin.py' ๐
admin.site.register(Song)