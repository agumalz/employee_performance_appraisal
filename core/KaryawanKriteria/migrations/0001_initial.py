# Generated by Django 5.0.6 on 2024-08-10 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crew', '0005_delete_nilaikriteria'),
        ('kriteria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KaryawanKriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.FloatField()),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penilaian', to='crew.crew')),
                ('kriteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kriteria.kriteria')),
            ],
            options={
                'unique_together': {('karyawan', 'kriteria')},
            },
        ),
    ]
