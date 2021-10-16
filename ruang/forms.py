from django import forms
from .models import Ruang



class RuangForm(forms.ModelForm):
	class Meta:
		model = Ruang
		fields = [
			'ID_Ruang',
			'Ruangan',
			'PJ_Ruang',
			'Gedung',
		]
