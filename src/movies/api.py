from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from movies.models import Movie
from movies.serializers import MoviesListSerializer, MovieSerializer


class MoviesListAPI(ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MoviesListSerializer

    def get_serializer_class(self):
        return MoviesListSerializer if self.request.method == 'GET' else MovieSerializer


class MovieDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
