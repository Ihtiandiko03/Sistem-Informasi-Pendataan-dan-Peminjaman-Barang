from django import forms
from .models import Barang

class BarangForm(forms.ModelForm):
	class Meta:
		model = Barang
		fields = [
			'ID_Detail',
			'Kode_Barang',
			'Nama_Barang',
			'Merk',
			'Stock',
			'BAP_Kedatangan',
		]
