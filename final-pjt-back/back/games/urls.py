from django.urls import path
from . import views

urlpatterns = [
    path('tetris/', views.tetris),
    path('snake/', views.snake),
    path('2048/', views.game_2048),
]
