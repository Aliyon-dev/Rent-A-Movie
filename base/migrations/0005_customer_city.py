# Generated by Django 5.0.6 on 2024-06-11 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_genre_alter_movie_id_alter_movie_price_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]