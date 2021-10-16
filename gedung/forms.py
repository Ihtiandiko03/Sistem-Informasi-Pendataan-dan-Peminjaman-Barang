from django import forms
from .models import Gedung

class GedungForm(forms.ModelForm):
	class Meta:
		model = Gedung
		fields=[
			'ID_Gedung',
			'Nama_Gedung',
			'PJ_Gedung',
		]