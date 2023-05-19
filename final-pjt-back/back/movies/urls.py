from django.urls import path
from . import views

urlpatterns = [
    path('movie/title/', views.get_movie_title),
    path('movie/alltitle/', views.get_movie_all_title),
    path('movie/', views.get_movie),
    path('movie/<int:movie_pk>/', views.get_movie_detail),
    path('review/<int:movie_pk>/', views.review),
    path('review/detail/<int:review_pk>/', views.review_detail),
    path('api_list/', views.api_list)
]
