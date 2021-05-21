from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_index_or_create),
    path('<int:movie_pk>/', views.movie_detail_or_update_or_delete),
    path('<int:movie_pk>/movie_rank/', views.movie_rank_index_or_create),
    path('<int:movie_pk>/movie_rank/<int:movie_rank_pk>/', views. movie_rank_detail_or_update_or_delete),
]
