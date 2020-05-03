from django.urls import path
from . import views

urlpatterns = [
    path('', views.experience, name='experience'),
    path('AddReview/', views.new_review, name='new_review'),
    path('Review/<str:id>/', views.view_review, name='view_review'),
    path('Review/<str:id>/like/', views.like, name='like'),
    path('Review/<str:id>/update/', views.update_review, name='update_review'),
    path('Review/<str:id>/remove/', views.delete_review, name='delete_review'),
]
