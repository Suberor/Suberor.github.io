# Generated by Django 4.1.7 on 2023-02-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FamilyApp', '0014_spellsreseñas_remove_spells_opinion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spellsreseñas',
            name='nombre',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='spellsreseñas',
            name='usuario',
            field=models.CharField(default='', max_length=40),
        ),
    ]
