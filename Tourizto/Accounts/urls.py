from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginview, name='loginview'),
    path('logout/', views.logoutview, name='logoutview'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
]

