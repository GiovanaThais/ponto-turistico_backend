# Generated by Django 3.2.1 on 2021-05-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0005_delete_avaliacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='notas',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]
