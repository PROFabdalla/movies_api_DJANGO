# Generated by Django 4.1.1 on 2022-10-01 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_movierating_movie_alter_movierating_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratingauther', to='main.watcher'),
        ),
    ]