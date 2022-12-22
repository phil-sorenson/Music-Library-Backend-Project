from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_songs_list),
    path('', views.post_song),
        # Looking to return a specific song w/ its PK/ID # so allowing 'strings' to be the PK in the URL for GET requests via can cause problems
            # SOLUTION: 👇 int: in front of pk 
    path('<int:pk>', views.song_detail),
]