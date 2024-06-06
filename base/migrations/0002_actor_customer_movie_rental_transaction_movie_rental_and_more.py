# Generated by Django 5.0.6 on 2024-06-05 18:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=50)),
                ('Lname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=50)),
                ('Lname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('movie_type', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
                ('release_year', models.DateField()),
                ('language', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateField()),
                ('rental_expiry', models.DateField()),
                ('rental_cost', models.IntegerField()),
                ('rental_cost_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField()),
                ('Price', models.IntegerField()),
                ('Tax', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie_rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MovieID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.movie')),
                ('RentalID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.rental')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.customer')),
                ('TransactionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.actor')),
                ('MovieID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.movie')),
            ],
            options={
                'unique_together': {('ActorID', 'MovieID')},
            },
        ),
    ]