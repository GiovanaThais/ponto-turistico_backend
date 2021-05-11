# Generated by Django 3.2.1 on 2021-05-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=150, verbose_name='rua')),
                ('bairro', models.CharField(max_length=100, verbose_name='bairro')),
                ('cidade', models.CharField(max_length=120, verbose_name='cidade')),
                ('estado', models.CharField(max_length=150, verbose_name='estado')),
                ('pais', models.CharField(max_length=70, verbose_name='país')),
                ('complementos', models.CharField(blank=True, max_length=100, null=True, verbose_name='complementos')),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
