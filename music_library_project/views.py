from rest_framework.decorators import api_view
from rest_framework.response import Response
# We want to try to avoid 'Hard-Coding' the status numbers (i.e 'return Response(serializer.data, status = 201)') SOLUTION BELOW 📝👇
from rest_framework import status
from .models import Song
from .serializers import SongSerializer

# Since POST will be using the same 'endpoint(URL)' as GET, we are able to put them in the same function
@api_view(['GET', 'POST'])
def songs_list(request):
    if request.method == 'GET':
            # Query to GET all of the songs from database
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
            # Code above👆(Creating the serializer) takes all the songs that were queried and converts it to a "Python dictionary"
                # "many=True" is telling the serializer that it will have to serialize potentially thousands/millions of song objects
            # all information/objects queried comes back as "data"👇(hence why we want to return 'serializer.data' below)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
            # Query to CREATE/POST a new song to database/list
            # CODE THOUGHT PROCESS: What do we have to do/implement to ACCEPT the POST/request for a new Song object
                # 'request.data' == The POST request sent in from Postman or some other API site
        serializer = SongSerializer(data = request.data)

            # Before accepting incoming data from POST request, We MUST VALIDATE(📝👇)--make sure it is not 'dirty' or containing incorrect information (e.g. 'name' instead of 'title')
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    


