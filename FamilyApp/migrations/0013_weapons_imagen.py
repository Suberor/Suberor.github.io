# Generated by Django 4.1.7 on 2023-02-23 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FamilyApp', '0012_alter_spells_descripcion_alter_spells_opinion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapons',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
