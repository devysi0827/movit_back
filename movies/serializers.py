from rest_framework import serializers
from .models import Movie, MovieRank


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

class MovieRankSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MovieRank
        fields = ('rank',)