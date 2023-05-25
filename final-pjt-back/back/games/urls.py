from django.urls import path
from . import views

urlpatterns = [
    path('tetris/<int:user_pk>', views.tetris),
    path('snake/<int:user_pk>', views.snake),
    path('2048/<int:user_pk>', views.game_2048),
]
