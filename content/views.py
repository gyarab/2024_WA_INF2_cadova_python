import json
from django.shortcuts import render
from django.http import HttpResponse

import requests
# data = [
#     {
#         'title': 'web Gymnazia Arabska',
#         'link': 'https://gyarab.cz',
#     },
#     {
#         'title': 'web jutub',
#         'link': 'https://youtube.com',
#     },
# ]

def homepage(request):
    with open('articles.json', encoding='utf-8') as f:
        data = json.load(f)

    article_html = ''
    i=0
    for article in data:
        title = article['title']
        image = article['image']
        article_html += f'<h2><a href="{article["link"]}">{article["title"]}</a></h2>'
        article_html += f'<img src="{article["image"]}" alt="{article["title"]}">'
        i+=1

    return HttpResponse(article_html)

def articles(request):
    with open('articles.json', encoding='utf-8') as f:
        data = json.load(f)

    article = articles[id]
    title = article['title']
    perex = article['perex']
    image = article['image']

    return HttpResponse(f"""<h2>{title}</h2><img src="{image}" alt="{title}"><p>{perex}</p><a href="/">Zpět na úvodní stránku</a>""")        

def hello(request):
    return HttpResponse('Hello world!')

def vynasob(request, a, b):
    return HttpResponse(f'{a} * {b} = {a*b}')

