from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=100)
    birth = models.TextField()
    image = models.URLField(max_length=500)
    info = models.TextField()
    
    def __str__(self):	
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()

    
    def __str__(self):	
        return self.name
    
# Create your models here.
class Band(models.Model):
    title = models.CharField(max_length=100)
    perex = models.TextField()
    image = models.URLField()
    creation = models.TextField()
    singer = models.CharField(max_length=100)
    link = models.URLField()
    genre = models.CharField(max_length=100)
    
    def __str__(self):	
        return self.title