# Generated by Django 3.2.1 on 2021-05-06 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='aprovado',
            field=models.BooleanField(default=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(verbose_name='comentários'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='data',
            field=models.DateField(auto_now_add=True, verbose_name='data'),
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=3)),
                ('data', models.DateField(auto_now_add=True, verbose_name='nota')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Avaliaçao',
                'verbose_name_plural': 'Avaliaçoes',
                'db_table': 'avaliacao',
            },
        ),
    ]
