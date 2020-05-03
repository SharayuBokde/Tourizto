from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='pics')
    likes = models.ManyToManyField(User, related_name='review_likes', blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ['-time_stamp']
    
    def __str__(self):
        return self.title 
