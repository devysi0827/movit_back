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
    genre_ids = models.CharField(max_length=200)
    # 'genre_ids': [28/ 12/ 53/ 10752]
    # 형규님네 python 미리 데이터를 받은 다음에 더미데이터를 json 그거를 불러와서 쓴다!
    # 맨 처음에는 쓸 필요 x

    # 일회성데이터에서는 vue에서 api를 불러오고////, 여러분 반복할 데이터, user가 포함된 데이터는 장고db를 사용한다.

    # 정원님네 vue 시작할때 요청을 해서 받은 데이터 이걸 장고db에 저장을 해서 필요할때 확인한다. ==> 배열 받는 방법을 모르겠다(v)
    # 
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
