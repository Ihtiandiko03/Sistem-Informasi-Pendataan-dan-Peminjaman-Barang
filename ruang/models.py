from django.db import models
from gedung.models import Gedung

# Create your models here.
class Ruang(models.Model):
	id=models.IntegerField()
	ID_Ruang = models.CharField(max_length=20)
	Ruangan = models.CharField(max_length=10, primary_key=True)
	PJ_Ruang = models.CharField(max_length=50)
	Gedung = models.ForeignKey(Gedung, on_delete=models.CASCADE)

	def __str__ (self):
		return "{}".format(self.Ruangan)