# Generated by Django 3.1.3 on 2020-11-28 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_computadoras', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarjetamemoriaram',
            old_name='tamaño',
            new_name='tamano',
        ),
    ]
