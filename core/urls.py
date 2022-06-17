from django.urls import path
from .views import index, mangas, manga

urlpatterns = [
    path('', index, name='index'),
    path('mangas/', mangas, name='mangas'),
    path('manga/<int:id>', manga, name='manga')
]