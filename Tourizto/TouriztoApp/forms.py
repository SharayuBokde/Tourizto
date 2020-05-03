from django.forms import ModelForm
from .models import Destination

class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = [
            'name',
            'state',
            'duration',
            'tagline',
            'abstract',
            'image',
            'description',
            'highlights',
            'itenary_titles',
            'itenary',
            'price',
            'offer',
            'discount'
        ]


















        