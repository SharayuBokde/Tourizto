from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    abstract = models.CharField(max_length=500)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='pics')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-time_stamp']
    
    def __str__(self):
        return self.title 

class Image(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,)
    display_image = models.ImageField(upload_to='pics', blank=True, null=True)

    def __str__(self):
        return self.blog.title + 'Images'
