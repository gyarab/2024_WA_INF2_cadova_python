from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    perex = models.TextField()
    image = models.URLField()
    creation = models.TextField()
    singer = models.CharField(max_length=100)
    link = models.URLField()
    genre = models.CharField(max_length=100)
    