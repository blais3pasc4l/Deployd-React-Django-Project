# Generated by Django 4.0.2 on 2022-03-01 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='dirección',
            new_name='direccion',
        ),
    ]
