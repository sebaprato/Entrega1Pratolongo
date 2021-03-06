# Generated by Django 4.0.4 on 2022-06-01 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plato', models.CharField(max_length=40)),
                ('categoria', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reseñas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plato', models.CharField(max_length=40)),
                ('sabor', models.IntegerField()),
                ('presentacion', models.IntegerField()),
                ('calidad_precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('categoria', models.CharField(max_length=40)),
                ('ubicacion', models.CharField(max_length=40)),
                ('capacidad', models.IntegerField()),
            ],
        ),
    ]
