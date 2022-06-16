from django.db import models


class Manga(models.Model):
    STATUS_CHOICES = (
        ('L', 'Lançamento'),
        ('F', 'Finalizado'),
        ('I', 'Indefinido'),
    )
    nome = models.CharField(name='Nome', max_length=100)
    capitulos = models.IntegerField(name='Capitulos')
    genero = models.CharField(name='Genero', max_length=100)
    status = models.CharField(name='Status', max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nome