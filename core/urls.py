from django.urls import path
from .views import index, mangas

urlpatterns = [
    path('', index, name='index'),
    path('mangas/', mangas, name='mangas')
]