from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
import requests
from .models import FavouriteImage
from django.core import serializers


# Create your views here.
def home(request):
    return render(request, 'searchimages/home.html')

class SearchImages(APIView):

    def get(self,request, format = None):
        lat = request.query_params['lat']
        lon = request.query_params['lon']

        response = requests.get(f'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=0bfbc9a68bd9f1a4bc6c8f7501d9920a&lat={lat}&lon={lon}&format=json&nojsoncallback=1&per_page=10&accuracy=1')
        images = response.json()
        message = {
            'Response': 200,
            'Message': 'Get Search Images',
            'Data':    images['photos']['photo']
        }
        return Response(message)

class FavouriteImages(APIView):

    def get(self,request, format = None):
        imageList = FavouriteImage.objects.all()
        print(imageList)
        imageUrlList = []
        for i in range(len(imageList)):
            imageUrlList.append(imageList[i].imageUrl)
        message = {
            'Response': 200,
            'Message': 'Get Search Images',
            'Data':   imageUrlList 
        }
        return Response(message)

    def post(self,request, format = None):
        data = request.data
        imageUrl = data.get('imageUrl',None)
        # Add image url to database
        FavouriteImag = FavouriteImage(imageUrl=imageUrl)
        FavouriteImag.save()
        message = {
            'Response': 200,
            'Message': 'Add To Wish List',
            'data':    imageUrl
        }
        return Response(message)