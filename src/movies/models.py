from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # optional

    def __str__(self):
        """
        :return: La representación de un objeto como un string
        """
        return self.name


class Movie(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=150)
    summary = models.TextField()
    director_name = models.CharField(max_length=150)
    release_date = models.DateField()
    image = models.URLField()
    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación del registro
    modified_at = models.DateTimeField(auto_now=True)  # Graba la fecha de la última modificación

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        """
        :return: La representación de un objeto como un string
        """
        return self.title
