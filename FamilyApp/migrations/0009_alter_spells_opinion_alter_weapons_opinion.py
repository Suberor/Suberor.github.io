# Generated by Django 4.1.7 on 2023-02-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FamilyApp', '0008_spells_descripcion_spells_opinion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spells',
            name='opinion',
            field=models.TextField(default='Nadie ha opinado sobre este hechizo aún.', max_length=1000),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='opinion',
            field=models.TextField(default='Nadie ha opinado sobre esta arma aún.', max_length=1000),
        ),
    ]
