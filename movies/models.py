from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField

# Create your models here.
class Movie(models.Model):
    adult = models.BooleanField(null=True, blank=True)
    backdrop_path = models.CharField(max_length=100, null=True, blank=True)
    # views에서 처리하자
    # genre_ids = ArrayField(ArrayField(models.IntegerField()))
    # genre_ids = JSONField(default=[] ,null=True, blank=True)
    # genre_ids = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
    # genre_ids = models. 'genre_ids': [28/ 12/ 53/ 10752] 
    # movie_id = models.IntegerField()
    original_language = models.CharField(max_length=100, null=True, blank=True)
    original_title = models.CharField(max_length=100, null=True, blank=True)
    overview = models.CharField(max_length=100, null=True, blank=True) 
    popularity = models.IntegerField(null=True, blank=True) 
    poster_path = models.CharField(max_length=200, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True) 
    title = models.CharField(max_length=100)
    video = models.BooleanField(null=True, blank=True)
    vote_average = models.IntegerField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)

# {'adult': False, 
# 'backdrop_path': '/fPGeS6jgdLovQAKunNHX8l0avCy.jpg', 
# 'genre_ids': [28, 12, 53, 10752], 
# 'id': 567189, 
# 'original_language': 'en',
# 'original_title': "Tom Clancy's Without Remorse",
# 'overview': 'An elite Navy SEAL uncovers an international conspiracy while seeking justice for the murder of his pregnant wife.', 'popularity': 2425.841, 'poster_path': '/rEm96ib0sPiZBADNKBHKBv5bve9.jpg',
# 'release_date': '2021-04-29', 
# 'title': "Tom Clancy's Without Remorse", 
# 'video': False, 
# 'vote_average': 7.3, 
# 'vote_count': 907

class MovieRank(models.Model):
    
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_rank')
    rank = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])
