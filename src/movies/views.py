# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.views.generic import ListView

from movies.models import Movie
from movies.forms import MovieForm


@login_required
def hello_world(request):
    return HttpResponse("Hello World!")


@login_required
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


class CreateMovieView(View):

    def get(self, request):
        form = MovieForm()
        return render(request, "movie_form.html", {"form": form})

    def post(self, request):
        movie = Movie()
        movie.user = request.user  # Asignamos el usuario autenticado
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            form = MovieForm()
            url = reverse("movie_detail_page", args=[movie.pk])
            message = "Película guardada!"
            message += "<a href='{0}'>View</a>".format(url)
            messages.success(request, message)
        return render(request, "movie_form.html", {"form": form})


class MyMoviesView(ListView):

    model = Movie
    template_name = "my_movies.html"
