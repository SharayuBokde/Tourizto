from django.urls import path
from . import views

urlpatterns = [
    path('', views.travelouge, name='travelouge'),
    path('AddBlog/', views.new_blog, name='new_blog'),
    path('Blog/<str:id>/', views.view_blog, name='view_blog'),
    path('Blog/<str:id>/like/', views.like, name='like'),
    path('Blog/<str:id>/update/', views.update_blog, name='update_blog'),
    path('Blog/<str:id>/remove/', views.delete_blog, name='delete_blog'),
]
