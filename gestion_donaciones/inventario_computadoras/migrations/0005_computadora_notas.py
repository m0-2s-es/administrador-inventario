# Generated by Django 3.1.3 on 2020-11-28 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_computadoras', '0004_computadora'),
    ]

    operations = [
        migrations.AddField(
            model_name='computadora',
            name='notas',
            field=models.CharField(blank=True, max_length=140),
        ),
    ]