from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from autoslug import AutoSlugField
import datetime

class Uk_Negara(models.Model): # Tabel Negara
	nama_negara = models.CharField(max_length=64, unique=True, blank=False)
	description = models.TextField('Description', blank=True)

	def __unicode__(self):	# Python 3: def __str__(self):
		return self.nama_negara
		
class Uk_Provinsi(models.Model): # Tabel Provinsi
	negara = models.ForeignKey(Uk_Negara)
	nama_provinsi = models.CharField(max_length=64, unique=True, blank=False)
	description = models.TextField('Description', blank=True)

	def __unicode__(self):	# Python 3: def __str__(self):
		return self.nama_provinsi
		
class Uk_Kota(models.Model): # Tabel Kota
	provinsi = models.ForeignKey(Uk_Provinsi)
	nama_kota = models.CharField(max_length=64, blank=False)
	description = models.TextField('Description', blank=True)

	def __unicode__(self):	# Python 3: def __str__(self):
		return self.nama_kota
		
class Uk_Bank(models.Model): # Tabel Nama Bank
	nama_bank = models.CharField(max_length=128, unique=True)
	description = models.TextField('Description', blank=True)

	def __unicode__(self):	# Python 3: def __str__(self):
		return self.nama_bank
		
class Uk_Toko(models.Model): # Tabel Toko
	YA = 'y'
	TIDAK = 'n' 
	
	STATUS_CHOICES = (
    (YA, 'Aktif'),
    (TIDAK, 'Tidak Aktif'),
    )
	
	nama_toko = models.CharField(max_length=128, unique=True)
	alamat_toko = models.TextField()
	kota = models.ForeignKey(Uk_Kota)
	provinsi = models.ForeignKey(Uk_Provinsi)
	telepon_toko = models.CharField(max_length=16)
	email_toko = models.CharField(max_length=128)
	logo_toko = models.ImageField(upload_to='logo_toko', blank=True)
	create_date = models.DateTimeField()
	status_toko = models.CharField(max_length=1, choices=STATUS_CHOICES, default=YA)
	description = models.TextField('Description', blank=True)

	def __unicode__(self):	# Python 3: def __str__(self):
		return self.nama_toko
		
class Uk_Bank_Account(models.Model): # Tabel Account Bank
	toko = models.ForeignKey(Uk_Toko)
	bank_account = models.ForeignKey(Uk_Bank)
	norek_account = models.CharField(max_length=64, unique=True)
	nama_account = models.CharField(max_length=128)
	description = models.TextField('Description', blank=True)

	def __unicode__(self):	# Python 3: def __str__(self):
		return self.norek_account
		
class User_Profile(models.Model): # Tabel profile user
	LAKI = 'l'
	PEREMPUAN = 'p'
	YES = 'y'
	NO = 'n'
	
	GENDER_CHOICES = (
	(LAKI, 'Laki-laki'),
	(PEREMPUAN, 'Perempuan'),
	)
	
	ADMIN_USER_CHOICES = (
	(YES, 'Ya'),
	(NO, 'Tidak'),
	)
	
	user = models.OneToOneField(User, unique=True)
	nama_lengkap = models.CharField(max_length=150)
	jenis_kelamin = models.CharField(max_length=1, choices=GENDER_CHOICES, default=LAKI)
	tgl_lahir = models.DateField()
	negara = models.ForeignKey(Uk_Negara)
	provinsi = models.ForeignKey(Uk_Provinsi)
	kota = models.ForeignKey(Uk_Kota)
	alamat	= models.TextField()
	toko_id = models.ForeignKey(Uk_Toko, null=True)
	is_user_admin = models.CharField(max_length=1, choices=ADMIN_USER_CHOICES, default=NO)

	def __unicode__(self):	# Python 3: def __str__(self):
		return self.nama_lengkap
		
class Uk_Produk(models.Model): # Tabel Product
	YA = 'y'
	TIDAK = 'n' 
	
	STATUS_CHOICES = (
    (YA, 'Aktif'),
    (TIDAK, 'Tidak Aktif'),
    )
	
	toko = models.ForeignKey(Uk_Toko)
	nama_produk = models.CharField(max_length=256)
	deskripsi_produk = models.TextField('Keterangan', blank=True)
	harga = models.CharField(max_length=64)
	nama_seo = models.CharField(max_length=256)
	create_date = models.DateField()
	status_toko = models.CharField(max_length=1, choices=STATUS_CHOICES, default=YA)

	def __unicode__(self):	# Python 3: def __str__(self):
		return self.nama_produk
		
class Uk_Produk_Image(models.Model): # Tabel Product Image
	produk = models.ForeignKey(Uk_Produk)
	image = models.ImageField(upload_to='image_produk', blank=True)
	
	def __unicode__(self):	# Python 3: def __str__(self):
		return self.image
		
class Uk_Produk_Option_Group(models.Model): # Tabel Product Option Group
	produk = models.ForeignKey(Uk_Produk)
	option_group_name = models.CharField(max_length=256)
	
	def __unicode__(self):	# Python 3: def __str__(self):
		return self.option_group_name
		
class Uk_Produk_Option(models.Model): # Tabel Product Option
	option_group = models.ForeignKey(Uk_Produk_Option_Group)
	option = models.CharField(max_length=256)
	
	def __unicode__(self):	# Python 3: def __str__(self):
		return self.option
