from app.views import index, sobre
from django.urls import path

app_urls = [
    path('', index, name='index'),
    path('sobre', sobre, name='sobre'),
]
