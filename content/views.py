from django.shortcuts import render
from django.http import HttpResponse

from .models import Band, Genre, Singer

import requests
import json

def homepage(request):
    articles = Band.objects.all()

    return render(request, 'content/homepage.html', {'articles': articles})

def band(request, id):
    with open('articles.json', encoding='utf-8') as f:
        bands = json.load(f)

    band = bands[id]
    return render(request, 'content/article.html', {'article': band})

def genre(request, id):
    with open('articles.json', encoding='utf-8') as f:
        genres = json.load(f)

    genre = genres[id]
    return render(request, 'content/article.html', {'article': genre})

def singer(request, id):    
    with open('articles.json', encoding='utf-8') as f:
        singers = json.load(f)

    singer = singers[id]
    return render(request, 'content/singer.html', {'singer': singer})