# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Uk_Kota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_kota', models.CharField(max_length=100)),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Uk_Negara',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_negara', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Uk_Provinsi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_provinsi', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('negara', models.ForeignKey(to='ukm_project.Uk_Negara')),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_lengkap', models.CharField(max_length=150)),
                ('jenis_kelamin', models.CharField(default=b'l', max_length=1, choices=[(b'l', b'Laki-laki'), (b'p', b'Perempuan')])),
                ('tgl_lahir', models.DateField(auto_now=True)),
                ('alamat', models.TextField()),
                ('kota', models.ForeignKey(to='ukm_project.Uk_Kota')),
                ('negara', models.ForeignKey(to='ukm_project.Uk_Negara')),
                ('provinsi', models.ForeignKey(to='ukm_project.Uk_Provinsi')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='uk_kota',
            name='provinsi',
            field=models.ForeignKey(to='ukm_project.Uk_Provinsi'),
        ),
    ]
