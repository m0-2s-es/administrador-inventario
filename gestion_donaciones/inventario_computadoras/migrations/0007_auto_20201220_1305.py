# Generated by Django 3.1.3 on 2020-12-20 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_computadoras', '0006_auto_20201214_0245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computadora',
            old_name='sistema_operativo',
            new_name='sist_op',
        ),
    ]
