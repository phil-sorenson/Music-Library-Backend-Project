from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer


@api_view(['GET'])
def songs_list(request):
    # Query to get all of the songs from database
    songs = Song.objects.all()

    serializer = SongSerializer(songs, many=True)
    # Code above👆(Creating the serializer) takes all the songs that were queried and converts it to a "Python dictionary"
        # "many=True" is telling the serializer that it will have to serialize potentially thousands/millions of song objects
    # all information/objects queried comes back as "data"👇(hence why we want to return 'serializer.data' below)

    return Response(serializer.data)