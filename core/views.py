from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def mangas(request):
    return render(request, 'mangas.html')
