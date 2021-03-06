from django.contrib import admin
from .models import Manga


class MangaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'capitulos', 'genero', 'status', 'autor']


admin.site.register(Manga, MangaAdmin)
