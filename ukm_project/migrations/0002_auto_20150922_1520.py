# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ukm_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uk_Bank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_bank', models.CharField(unique=True, max_length=128)),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Uk_Bank_Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('norek_account', models.CharField(unique=True, max_length=64)),
                ('nama_account', models.CharField(max_length=128)),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('bank_account', models.ForeignKey(to='ukm_project.Uk_Bank')),
            ],
        ),
        migrations.CreateModel(
            name='Uk_Produk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_produk', models.CharField(max_length=256)),
                ('deskripsi_produk', models.TextField(verbose_name=b'Keterangan', blank=True)),
                ('harga', models.CharField(max_length=64)),
                ('nama_seo', models.CharField(max_length=256)),
                ('create_date', models.DateField()),
                ('status_toko', models.CharField(default=b'y', max_length=1, choices=[(b'y', b'Aktif'), (b'n', b'Tidak Aktif')])),
            ],
        ),
        migrations.CreateModel(
            name='Uk_Produk_Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'image_produk', blank=True)),
                ('produk', models.ForeignKey(to='ukm_project.Uk_Produk')),
            ],
        ),
        migrations.CreateModel(
            name='Uk_Produk_Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Uk_Produk_Option_Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option_group_name', models.CharField(max_length=256)),
                ('produk', models.ForeignKey(to='ukm_project.Uk_Produk')),
            ],
        ),
        migrations.CreateModel(
            name='Uk_Toko',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_toko', models.CharField(unique=True, max_length=128)),
                ('alamat_toko', models.TextField()),
                ('telepon_toko', models.CharField(max_length=16)),
                ('email_toko', models.CharField(max_length=128)),
                ('logo_toko', models.ImageField(upload_to=b'logo_toko', blank=True)),
                ('create_date', models.DateTimeField()),
                ('status_toko', models.CharField(default=b'y', max_length=1, choices=[(b'y', b'Aktif'), (b'n', b'Tidak Aktif')])),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='user_profile',
            name='is_user_admin',
            field=models.CharField(default=b'n', max_length=1, choices=[(b'y', b'Ya'), (b'n', b'Tidak')]),
        ),
        migrations.AlterField(
            model_name='uk_kota',
            name='nama_kota',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='uk_negara',
            name='nama_negara',
            field=models.CharField(unique=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='uk_provinsi',
            name='nama_provinsi',
            field=models.CharField(unique=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='tgl_lahir',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='uk_toko',
            name='kota',
            field=models.ForeignKey(to='ukm_project.Uk_Kota'),
        ),
        migrations.AddField(
            model_name='uk_toko',
            name='provinsi',
            field=models.ForeignKey(to='ukm_project.Uk_Provinsi'),
        ),
        migrations.AddField(
            model_name='uk_produk_option',
            name='option_group',
            field=models.ForeignKey(to='ukm_project.Uk_Produk_Option_Group'),
        ),
        migrations.AddField(
            model_name='uk_produk',
            name='toko',
            field=models.ForeignKey(to='ukm_project.Uk_Toko'),
        ),
        migrations.AddField(
            model_name='uk_bank_account',
            name='toko',
            field=models.ForeignKey(to='ukm_project.Uk_Toko'),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='toko_id',
            field=models.ForeignKey(to='ukm_project.Uk_Toko', null=True),
        ),
    ]
