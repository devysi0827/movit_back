from rest_framework import serializers
from .models import Movie, MovieRank


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title','genre_ids')

class MovieRankSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MovieRank
        fields = ('rank',)