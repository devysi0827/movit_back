from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from rest_framework.decorators import authentication_classes, permission_classes
from .models import Movie, MovieRank
from .serializers import MovieSerializer, MovieRankSerializer
import json
import requests

@api_view(['GET', 'POST'])
def movie_index_or_create(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
       
    elif request.method == "POST":
        serializer = MovieSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)        

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_or_update_or_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk =movie_pk)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = MovieSerializer(instance =movie, data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie = movie)
            return Response(serializer.data)

    elif request.method == "DELETE":
        movie.delete()
        data = {
            "success" : True,
            "message" : "삭제완료"
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def movie_rank_index_or_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk =movie_pk)
    
    if request.method == "GET":
        movie_ranks = MovieRank.objects.all()
        serializer = MovieRankSerializer(movie_ranks, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MovieRankSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status= status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_rank_detail_or_update_or_delete(request, movie_pk, movie_rank_pk):
    movie = get_object_or_404(Movie, pk =movie_pk)
    movie_rank = get_object_or_404(MovieRank, pk =movie_rank_pk)

    if request.method == "GET":
        serializer = MovieRankSerializer(movie_rank)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = MovieRankSerializer(instance = movie_rank, data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie_rank = movie_rank)
            return Response(serializer.data)

    elif request.method == "DELETE":
        movie_rank.delete()
        data = {
            "success" : True,
            "message" : "rank 삭제완료"
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)    

@api_view(['GET'])
def movies_save(request):
    get_movies = 'https://api.themoviedb.org/3/movie/popular?api_key=6b1e9899f17fa92429f5a793999dcb8f'
    response = requests.get(get_movies).json()
    for i in range(20):
        # print(2)
        now_movie = response['results'][i]
        genre_ids = str(now_movie['genre_ids'])
        # print(1)
        # print(now_movie['title'])
        # print(now_movie['id'])
        movie = {
            'title':now_movie['title'],
            'genre_ids':genre_ids,
            'adult': now_movie['adult'],
            'backdrop_path': now_movie['backdrop_path'],
            'movie_id': now_movie['id'],
            'original_language': now_movie['original_language'],
            'original_title': now_movie['original_title'],
            'overview': now_movie['overview'],
            'popularity': now_movie['popularity'],
            'poster_path': now_movie['poster_path'],
            'release_date': now_movie['release_date'],
            'video': now_movie['video'],
            'vote_average': now_movie['vote_average'],
            'vote_count': now_movie['vote_count'],
        }
        serializer = MovieSerializer(data=movie)
        # print(2)
        # print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    data = {
            "save" : True,
        } 
    return Response(data)

      