from django.contrib import admin
from .models import Peminjaman
from .models import DetailPeminjaman
# Register your models here.

admin.site.register(Peminjaman)
admin.site.register(DetailPeminjaman)