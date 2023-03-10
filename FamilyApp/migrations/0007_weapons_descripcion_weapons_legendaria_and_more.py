# Generated by Django 4.1.7 on 2023-02-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FamilyApp', '0006_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapons',
            name='descripcion',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='weapons',
            name='legendaria',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='weapons',
            name='opinion',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='weapons',
            name='puntaje',
            field=models.FloatField(default=0),
        ),
    ]
