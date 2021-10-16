from django.db import models

# Create your models here.
class Barang(models.Model):
	id=models.IntegerField()
	ID_Detail = models.CharField(max_length=100)
	Kode_Barang = models.IntegerField(primary_key=True)
	Nama_Barang = models.CharField(max_length=100)
	Merk = models.CharField(max_length=100)
	Stock = models.IntegerField()
	BAP_Kedatangan = models.ImageField()

	def __str__ (self):
		return "{}.{}".format(self.Kode_Barang, self.Nama_Barang)
