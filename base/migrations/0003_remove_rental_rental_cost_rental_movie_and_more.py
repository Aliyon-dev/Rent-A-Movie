# Generated by Django 5.0.6 on 2024-06-19 21:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_street_address_customer_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='rental_cost',
        ),
        migrations.AddField(
            model_name='rental',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.movie'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MovieRental',
        ),
    ]
