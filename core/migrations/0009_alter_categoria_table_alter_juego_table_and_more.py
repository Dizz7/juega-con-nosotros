# Generated by Django 5.2 on 2025-04-14 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_juego_categoria_alter_juego_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='categoria',
            table='core_categoria',
        ),
        migrations.AlterModelTable(
            name='juego',
            table='core_juego',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='core_usuario',
        ),
    ]
