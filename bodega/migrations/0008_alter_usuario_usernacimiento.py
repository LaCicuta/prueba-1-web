# Generated by Django 4.1.2 on 2024-07-19 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0007_alter_usuario_passwordusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='userNacimiento',
            field=models.DateField(),
        ),
    ]
