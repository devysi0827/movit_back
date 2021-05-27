from django.urls import path
from . import views


urlpatterns = [
    path('review_data/', views.review_data),
    path('', views.review_index_or_create),
    path('<int:review_pk>/', views.review_detail_or_update_or_delete),
    path('<int:review_pk>/comments/', views.review_comment_index_or_create),
    path('<int:review_pk>/comments/<int:comment_pk>/', views.review_comment_detail_or_update_or_delete),

]

