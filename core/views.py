from django.shortcuts import render
from .models import Manga

def index(request):
    return render(request, 'index.html')

def mangas(request):
    mang = Manga.objects.all()
    context = {
        'mang': mang
    }
    return render(request, 'mangas.html', context)
