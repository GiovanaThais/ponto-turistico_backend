# Generated by Django 3.2.1 on 2021-05-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_auto_20210505_1526'),
        ('core', '0002_auto_20210505_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.Atracao'),
        ),
    ]
