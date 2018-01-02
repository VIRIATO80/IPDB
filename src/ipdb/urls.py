"""ipdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from movies.views import home, movie_detail, CreateMovieView, MyMoviesView
from users.api import UserListAPI, UserDetailAPI
from users.views import logout, LoginView

urlpatterns = [
    path('', home, name="home_page"),
    path('movies/<int:pk>', movie_detail, name="movie_detail_page"),
    path('movies/createMovie', CreateMovieView.as_view(), name="create_movie_page"),
    path('movies/', MyMoviesView.as_view(), name="my_movies_page"),

    path('login/', LoginView.as_view(), name="login_page"),
    path('logout/', logout, name="logout_page"),

    path('admin/', admin.site.urls),

    # URLS para el API REST
    path('api/1.0/users/<int:pk>', UserDetailAPI.as_view(), name='api_user_detail'),
    path('api/1.0/users/', UserListAPI.as_view(), name='api_user_list')

]
