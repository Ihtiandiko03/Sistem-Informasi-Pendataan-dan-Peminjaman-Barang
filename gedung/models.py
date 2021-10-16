from django.db import models

# Create your models here.
class Gedung(models.Model):
	ID_Gedung = models.CharField(max_length=20)
	Nama_Gedung = models.CharField(max_length=100, primary_key=True)
	PJ_Gedung = models.CharField(max_length=50)

	def __str__ (self):
		return "{}".format(self.Nama_Gedung)
