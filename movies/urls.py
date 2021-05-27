from django.urls import path
from . import views


urlpatterns = [
    path('save/', views.movies_save),
    path('get_movie_info/', views.get_movie_info),
    path('get_rank_info/', views.get_rank_info),
    path('', views.movie_index_or_create),
    path('<int:movie_pk>/', views.movie_detail_or_update_or_delete),
    path('<int:movie_pk>/movie_rank/', views.movie_rank_index_or_create),
    path('<int:movie_pk>/movie_rank/<int:movie_rank_pk>/', views. movie_rank_detail_or_update_or_delete),
    
]
