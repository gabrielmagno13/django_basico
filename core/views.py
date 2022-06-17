from django.shortcuts import render, get_object_or_404
from .models import Manga

def index(request):
    return render(request, 'index.html')


def mangas(request):
    mang = Manga.objects.all()
    context = {
        'mang': mang
    }
    return render(request, 'mangas.html', context)


def manga(request, id):
    man = get_object_or_404(Manga, pk=id)
    context = {
        'man': man
    }
    return render(request, 'manga.html', context)

