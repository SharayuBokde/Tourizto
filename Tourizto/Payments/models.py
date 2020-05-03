from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from TouriztoApp.models import Destination

# Create your models here.
class Booking(models.Model):
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_email = models.EmailField()
    states = [
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    ]
    residence_state = models.CharField(max_length=100, choices=states)
    arrival_date = models.DateTimeField("Arrival Date (mm/dd/yyyy)", auto_now=False, auto_now_add=False)
    departure_date = models.DateTimeField("Departure Date (mm/dd/yyyy)", auto_now=False, auto_now_add=False)
    number_of_adults = models.IntegerField()
    number_of_children = models.IntegerField()
    food_choices = [
        ('VEG', 'Vegetarian'),
        ('NON-VEG', 'Non-Vegetarian')
    ]
    food_preference = models.CharField(max_length=10, choices=food_choices)
    accommodation = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    total_price = models.IntegerField()

    def __str__(self):
        return self.customer_name.username + ' Booking'
