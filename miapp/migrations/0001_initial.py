# Generated by Django 5.2 on 2025-04-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidop', models.CharField(max_length=100)),
                ('apellidom', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
    ]
