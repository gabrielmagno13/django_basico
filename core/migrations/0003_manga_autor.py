# Generated by Django 4.0.5 on 2022-06-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_manga_capitulos_remove_manga_genero_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='autor',
            field=models.CharField(default='some', max_length=50),
        ),
    ]