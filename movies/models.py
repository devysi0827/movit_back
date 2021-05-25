from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Movie(models.Model):
    adult = models.BooleanField(null=True, blank=True)
    backdrop_path = models.CharField(max_length=100, null=True, blank=True)
    genre_ids = models.CharField(max_length=200)
    movie_id = models.IntegerField(null=True, blank=True)
    original_language = models.CharField(max_length=100, null=True, blank=True)
    original_title = models.CharField(max_length=100, null=True, blank=True)
    overview = models.CharField(max_length=5000, null=True, blank=True) 
    popularity = models.FloatField(null=True, blank=True) 
    poster_path = models.CharField(max_length=5000, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True) 
    title = models.CharField(max_length=100)
    video = models.BooleanField(null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)

class MovieRank(models.Model):
    
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_rank')
    rank = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])
