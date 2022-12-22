from rest_framework.decorators import api_view
from rest_framework.response import Response
# We want to try to avoid 'Hard-Coding' the status numbers (i.e 'return Response(serializer.data, status = 201)') SOLUTION BELOW 📝👇
from rest_framework import status
from .models import Song
from .serializers import SongSerializer

# Since POST will be using the same 'endpoint(URL)' as GET, we are able to put them in the same function
@api_view(['GET'])
def get_songs_list(request):
    if request.method == 'GET':
            # Query to GET all of the songs from database
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
            # Code above👆(Creating the serializer) takes all the songs that were queried and converts it to a "Python dictionary"
                # "many=True" is telling the serializer that it will have to serialize potentially thousands/millions of song objects
            # all information/objects queried comes back as "data"👇(hence why we want to return 'serializer.data' below)
        return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['POST'])        
def post_song(request):
    if request.method == 'POST':
            # Query to CREATE/POST a new song to database/list
            #! CODE THOUGHT PROCESS: What do we have to do/implement to ACCEPT the POST/request for a new Song object
                # 'request.data' == The POST request sent in from Postman or some other API site
        serializer = SongSerializer(data = request.data)

            # Before accepting incoming data from POST request, We MUST VALIDATE(📝👇)--make sure it is not 'dirty' or containing incorrect information (e.g. 'name' instead of 'title')
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
            # Built in Django/serializer functionality - 'raise_exception=True' (📝👆) is the shortened version of the code below (No 'IF Statement' needed)
                #* if serializer.is_valid() == True:
                #*     serializer.save()
                #*     return Response(serializer.data, status = status.HTTP_201_CREATED)
                #* else:
                #*     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def song_detail(request, pk):
        #! CODE THOUGHT PROCESS: How can we connect this function to a specific endpoint in order to GET a specific Song object/'pk' (Primary Key)
            #! Create a specific url path via urls.py w/ <pk> involved
    try:   
        song = Song.objects.get(pk=pk)
            # get(pk=pk): Us telling Django look for the 'pk' from the songs table and return the one that is = to the pk parameter value
                # In case the inputted 'pk' is not found in the database table, we have to wrap our code in a Try/Except
        serializer = SongSerializer(song)
        return Response (serializer.data)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    
    


