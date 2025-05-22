from django.shortcuts import render
from django.http import HttpResponse

from .models import Band, Genre, Singer

import requests
import json

def homepage(request):
    bands = Band.objects.all()
    genres = Genre.objects.all()
    singers = Singer.objects.all()

    return render(request, 'content/homepage.html', {'bands': bands, 'genres': genres, 'singers': singers})

def band(request, id):
    with open('content/fixtures/bands.json', encoding='utf-8') as f:
        bands = json.load(f)

    band = bands[id]
    return render(request, 'content/band.html', {'band': band})

def genre(request, id):
    with open('content/fixtures/bands.json', encoding='utf-8') as f:
        genres = json.load(f)

    genre = genres[id]
    return render(request, 'content/genre.html', {'genre': genre})

def singer(request, id):    
    with open('content/fixtures/bands.json', encoding='utf-8') as f:
        singers = json.load(f)

    singer = singers[id]
    return render(request, 'content/singer.html', {'singer': singer})