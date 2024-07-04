# Generated by Django 4.1.2 on 2024-07-04 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='idCiudad',
            field=models.AutoField(db_column='idCiudad', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='codepais',
            name='idCodPais',
            field=models.AutoField(db_column='idCodPais', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pais',
            name='idPais',
            field=models.AutoField(db_column='idPais', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rubro',
            name='idRubro',
            field=models.AutoField(db_column='idRubro', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sexo',
            name='idSexo',
            field=models.AutoField(db_column='idSexo', primary_key=True, serialize=False),
        ),
    ]
