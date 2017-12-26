# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie


def hello_world(request):
    return HttpResponse("Hello World!")


def home(request):
    latest_movies = Movie.objects.all().order_by("-release_date")
    context = {'movies': latest_movies}
    return render(request, "home.html", context)


def movie_detail(request, pk):
    possible_movie = Movie.objects.filter(pk=pk).select_related("category")
    if len(possible_movie) == 0:
        #  Mostramos un 404 error
        return render(request, "404.html", status=404)
    else:
        movie = possible_movie[0]
        context = {'movie': movie}
        return render(request, "movie_detail.html", context)

