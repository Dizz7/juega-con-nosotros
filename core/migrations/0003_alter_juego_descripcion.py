# Generated by Django 5.2 on 2025-04-12 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_categoria_juego_imagen_juego_plataformas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
