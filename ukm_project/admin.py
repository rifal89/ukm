from django.contrib import admin
from ukm_project.models import Uk_Negara, Uk_Provinsi, Uk_Kota, Uk_Bank, Uk_Toko, Uk_Bank_Account, User_Profile, Uk_Produk, Uk_Produk_Image, Uk_Produk_Option_Group, Uk_Produk_Option

admin.site.site_header = "UKM Web Administration"
admin.site.register(Uk_Negara)
admin.site.register(Uk_Provinsi)
admin.site.register(Uk_Kota)
admin.site.register(Uk_Bank)
admin.site.register(Uk_Toko)
admin.site.register(Uk_Bank_Account)
admin.site.register(User_Profile)
admin.site.register(Uk_Produk)
admin.site.register(Uk_Produk_Image)
admin.site.register(Uk_Produk_Option_Group)
admin.site.register(Uk_Produk_Option)
