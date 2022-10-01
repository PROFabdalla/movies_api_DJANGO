# Generated by Django 4.1.1 on 2022-10-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_watchmovies_watcher_watchmovies_watcher'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='watcher',
            field=models.ManyToManyField(related_name='movies', to='main.watcher'),
        ),
        migrations.DeleteModel(
            name='WatchMovies',
        ),
    ]
