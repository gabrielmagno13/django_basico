from django.db import models


class Manga(models.Model):
    STATUS_CHOICES = (
        ('Em lançamento'),
        ('Finalizado'),
        ('Em hiato')
    )
    nome = models.CharField('Nome', max_length=100)
    capitulos = models.IntegerField('Capitulos')
    genero = models.CharField('Genero', max_length=100)
    status = models.CharField('Status', max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nome