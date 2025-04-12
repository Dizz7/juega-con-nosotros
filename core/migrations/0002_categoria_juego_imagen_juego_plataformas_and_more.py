# Generated by Django 5.2 on 2025-04-12 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('lema', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('imagen', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='juego',
            name='imagen',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='juego',
            name='plataformas',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='juego',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.categoria'),
        ),
    ]
