# Generated by Django 4.2.1 on 2023-05-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheronov_app', '0003_rename_film_director_notefilm_director_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notefilm',
            name='movie_viewed',
        ),
        migrations.AlterField(
            model_name='notefilm',
            name='promo',
            field=models.CharField(max_length=1000, verbose_name='promo'),
        ),
    ]
