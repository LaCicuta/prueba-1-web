# Generated by Django 4.1.2 on 2024-07-19 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0005_remove_usuario_idcodpais_delete_codepais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
