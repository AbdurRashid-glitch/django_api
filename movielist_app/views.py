from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse
# Create your views here.

# Created a func based view and store all the query objects into movies variable, then convert it into list and store it in a dictionary and finally return it as a Json response object data


def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)
