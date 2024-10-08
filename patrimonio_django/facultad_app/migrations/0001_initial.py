# Generated by Django 5.0 on 2024-09-19 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sede_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_facultad', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('numero_acuerdo', models.CharField(blank=True, max_length=50, null=True)),
                ('historia', models.TextField(blank=True, null=True)),
                ('estado_conservacion', models.CharField(choices=[('bueno', 'Bueno'), ('malo', 'Malo'), ('regular', 'Regular')], default='bueno', max_length=50)),
                ('estructura', models.TextField(blank=True, null=True)),
                ('valores', models.TextField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facultades', to='sede_app.sede')),
            ],
        ),
        migrations.CreateModel(
            name='AreaFacultad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_area', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='facultad_app.facultad')),
            ],
        ),
    ]
