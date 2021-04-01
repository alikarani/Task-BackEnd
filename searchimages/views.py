from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
import requests

# Create your views here.
def home(request):
    return render(request, 'searchimages/home.html')

# global imagesData
# imagesData = []
class Images(APIView):

    def get(self,request, format = None):
        response = requests.get('https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=0bfbc9a68bd9f1a4bc6c8f7501d9920a&lat=36.7&lon=43.8&format=json&nojsoncallback=1&per_page=10&accuracy=1')
        images = response.json()
        # print()
        message = {
            'Response': 200,
            'Message': 'Get Search Images',
            'Data':    images['photos']['photo']
        }
        return Response(message)
    
    def post(self,request, format = None):
        data = request.data
        imageUrl = data.get('imageUrl',None)
        # Add image url to database
        message = {
            'Response': 200,
            'Message': 'Add To Wish List',
            'data':    imageUrl
        }
        return Response(message)