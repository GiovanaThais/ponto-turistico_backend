# Generated by Django 3.2.1 on 2021-05-09 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_pontoturistico_avaliacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pontoturistico',
            old_name='Aprovado',
            new_name='status',
        ),
    ]
