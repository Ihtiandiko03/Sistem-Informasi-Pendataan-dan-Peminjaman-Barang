from django import forms
from .models import Peminjaman
from .models import DetailPeminjaman

class PeminjamanForm(forms.ModelForm):
	class Meta:
		model = Peminjaman
		fields = [
			'ID_Pinjam',
			'No_Peminjaman',
			'Kode_Barang',
			'Nama_Barang',
			'Jumlah',
			'Gedung',
			'Ruang',
		]

class DetailPeminjamanForm(forms.ModelForm):
	class Meta:
		model = DetailPeminjaman
		fields = [
			'ID_DetailPeminjaman',
			'No_Peminjaman',
			'NIP_NRK',
			'Nama_Pegawai',
			'Tgl_Pinjam',
			'Tgl_Kembali',
			'Berita_Acara_Peminjaman',
		]