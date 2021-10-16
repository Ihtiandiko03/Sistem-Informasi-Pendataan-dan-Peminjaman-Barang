from django.db import models
from staff.models import Pegawai
from gedung.models import Gedung
from ruang.models import Ruang
from barang.models import Barang

# Create your models here.

class DetailPeminjaman(models.Model):
	ID_DetailPeminjaman = models.CharField(max_length=20)
	No_Peminjaman = models.IntegerField(primary_key=True)
	NIP_NRK = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
	Nama_Pegawai = models.CharField(max_length=100)
	Tgl_Pinjam = models.DateField()
	Tgl_Kembali = models.DateField()
	Berita_Acara_Peminjaman = models.FileField()

	def __str__(self):
		return "{}.{}".format(self.No_Peminjaman, self.Nama_Pegawai)

class Peminjaman(models.Model):

	cek={
		('Baik', 'Baik'),
		('Sedang', 'Sedang'),
		('Rusak', 'Rusak'),
	}

	ID_Pinjam = models.CharField(max_length=20)
	No_Peminjaman = models.ForeignKey(DetailPeminjaman, on_delete=models.CASCADE)
	Kode_Barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
	Nama_Barang = models.CharField(max_length=20)
	Jumlah = models.IntegerField()
	Kondisi = models.CharField(max_length=20, choices=cek)
	Gedung = models.ForeignKey(Gedung, on_delete=models.CASCADE)
	Ruang  = models.ForeignKey(Ruang, on_delete=models.CASCADE)

	def __str__ (self):
		return "{}. {}. {}".format(self.id, self.ID_Pinjam, self.No_Peminjaman)