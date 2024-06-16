# Generated by Django 5.0.6 on 2024-06-16 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_zipcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zipcode',
            name='id',
        ),
        migrations.AlterField(
            model_name='zipcode',
            name='zip_code',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]