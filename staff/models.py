from django.db import models

# Create your models here.
class Pegawai(models.Model):
	jabatan = {
		('Dosen', 'Dosen'),
		('Mahasiswa', 'Mahasiswa'),
		('Tendik', 'Tendik'),
		('Pegawai', 'Pegawai'),
	}

	id=models.IntegerField()
	NIP_NRK = models.IntegerField(primary_key=True)
	nama_depan = models.CharField(max_length=100)
	nama_belakang = models.CharField(max_length=100)
	Alamat = models.TextField()
	Email = models.EmailField()
	Telp = models.CharField(max_length=15)
	Role = models.CharField(max_length=100, choices=jabatan)

	def __str__ (self):
		return "{}".format(self.NIP_NRK)


