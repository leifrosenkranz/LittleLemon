# Generated by Django 5.1.6 on 2025-02-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
