from django import forms
from .models import Pegawai

class PegawaiForm(forms.ModelForm):
	class Meta:
		model = Pegawai
		fields = [
			'NIP_NRK',
			'nama_depan',
			'nama_belakang',
			'Alamat',
			'Email',
			'Telp',
			'Role',
		]