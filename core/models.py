from django.db import models


class Manga(models.Model):
    STATUS_CHOICES = (
        ('L', 'Lançamento'),
        ('F', 'Finalizado'),
        ('I', 'Indefinido'),
    )
    nome = models.CharField(name='nome', max_length=100, default='some')
    capitulos = models.IntegerField(name='capitulos', default=1)
    genero = models.CharField(name='genero', max_length=10, default='some')
    status = models.CharField(name='status', max_length=1, choices=STATUS_CHOICES, default='L')

    def __str__(self):
        return self.nome