from django.urls import path
from . import views

urlpatterns = [
    path('booking/<int:id>/', views.booking, name='booking'),
    path('checkout/<int:id>/', views.checkout, name='checkout'),
    path('cart/<int:id>/',views.cart , name="cart"),
    path('charge/<int:id>/', views.charge, name="charge"),
    path('success/<int:id>', views.successMsg, name="success"),
    path('myBookings/', views.mybookings, name='mybookings'),
    path('confirm_order/<int:id>/', views.confirmation_mail, name='confirm_order'),
]
