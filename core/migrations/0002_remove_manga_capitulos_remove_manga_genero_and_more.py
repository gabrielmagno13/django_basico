# Generated by Django 4.0.5 on 2022-06-17 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='Capitulos',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='Genero',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='Nome',
        ),
        migrations.RemoveField(
            model_name='manga',
            name='Status',
        ),
        migrations.AddField(
            model_name='manga',
            name='capitulos',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='manga',
            name='genero',
            field=models.CharField(default='some', max_length=10),
        ),
        migrations.AddField(
            model_name='manga',
            name='nome',
            field=models.CharField(default='some', max_length=100),
        ),
        migrations.AddField(
            model_name='manga',
            name='status',
            field=models.CharField(choices=[('L', 'Lançamento'), ('F', 'Finalizado'), ('I', 'Indefinido')], default='L', max_length=1),
        ),
    ]
