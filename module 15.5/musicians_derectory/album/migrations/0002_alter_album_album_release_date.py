# Generated by Django 5.0 on 2024-01-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_release_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
