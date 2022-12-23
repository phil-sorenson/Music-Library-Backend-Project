from rest_framework.decorators import api_view
from rest_framework.response import Response
# We want to try to avoid 'Hard-Coding' the status numbers (i.e 'return Response(serializer.data, status = 201)') SOLUTION BELOW 📝👇
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Song
from .serializers import SongSerializer

# Since POST will be using the same 'endpoint(URL)' as GET, we are able to put them in the same function
@api_view(['GET','POST'])
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
            #! CODE THOUGHT PROCESS: What do we have to do/implement to ACCEPT the POST/request for a new Song object
                # 'request.data' == The POST request sent in from Postman or some other API site
        serializer = SongSerializer(data = request.data)

            # Before accepting incoming data from POST request, We MUST VALIDATE(📝👇)--make sure it is not 'dirty' or containing incorrect information (e.g. 'name' instead of 'title')
                # Built in Django/serializer functionality - 'raise_exception=True' (Shortcut for the 'If statement' code below)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

             #* ORIGINAL CODE (Before using the 'raise_exception=True shortcut)
                # if serializer.is_valid() == True:
                #     serializer.save()
                #     return Response(serializer.data, status = status.HTTP_201_CREATED)
                # else:
                #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
        # Place this duplicated line of code outside of if/elif statement so both methods use it (originally inside both 'GET' and 'PUT' methods)
    if request.method == 'GET':
            #! CODE THOUGHT PROCESS: How can we connect this function to a specific endpoint in order to GET a specific Song object/'pk' (Primary Key)
                #! Create a specific url path via urls.py w/ <pk> involved
            # W/ the 'get_object_or_404' shortcut(📝👆) we DO NOT need any of GET code below or the Try/Except(📝👇)
                # Inside the parameters of get_objects_or_404 the first item is the model you're requesting from (Song) and second is the GET statement (get(pk=pk))
                    # (pk=pk): Us telling Django look for the 'pk' from the songs table and return the one that is = to the pk parameter value
        serializer = SongSerializer(song)
        return Response(serializer.data)
                #* ORIGINAL CODE (Before using the get_object_or_404 shortcut)
                    # try:   
                    #     song = Song.objects.get(pk=pk)
                    #             # In case the inputted 'pk' is not found in the database table, we have to wrap our code in a Try/Except or the get_object_or_404 shorcut above
                    #     serializer = SongSerializer(song)
                    #     return Response (serializer.data)
                    # except Song.DoesNotExist:
                    #     return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
            #! CODE THOUGHT PROCESS (PUT(Update)): We want to get the original song from database via its 'pk/id' in order to make any changes/updates on it
                #! After making changes to that song/pk#, we want to return that Song object to the database with all the changes that we've made
                # Using serializer when updating something: =>   
                    # 1st: Pass in the current version of the object (song) 
                    # 2nd: Pass in the 'data' and set it = request.data 
                        # What that means: Takes in the updated JSON data and compare to current data/object
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
            #! CODE THOUGHT PROCESS (DELETE): This method will also use the 'song = get_object_or_404(Song, pk=pk)' because it is Deleting a specified requested pk #
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    
    


