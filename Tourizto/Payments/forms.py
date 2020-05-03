from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = [
            'residence_state',
            'departure_date',
            'arrival_date',
            'number_of_adults',
            'number_of_children',
            'food_preference',
            'accommodation',
        ]


















        