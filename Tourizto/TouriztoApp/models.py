from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=200, unique=True)
    state = models.CharField(max_length=100)
    duration = models.CharField(max_length=200)
    tagline = models.CharField(max_length=500)
    abstract = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    highlights = models.TextField()
    itenary_titles = models.TextField()
    itenary = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.name 

class Images(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='pics', blank=True, null=True)

    def __str__(self):
        return self.destination.name + 'Images'


