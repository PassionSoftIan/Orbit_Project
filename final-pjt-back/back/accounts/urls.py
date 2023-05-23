from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:user_pk>/', views.get_user),
    path('following/<int:user_pk>/', views.following),
    path('like/<int:review_pk>/', views.like_reviews),

]
