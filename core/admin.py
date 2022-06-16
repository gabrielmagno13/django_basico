from django.contrib import admin
from .models import Manga


class MangaAdmin(admin.ModelAdmin):
    list_display = ['Nome', 'Capitulos', 'Genero', 'Status']


admin.site.register(Manga, MangaAdmin)
