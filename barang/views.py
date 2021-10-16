from django.shortcuts import render, redirect

# Create your views here.
from .models import Barang
from .forms import BarangForm

def list(request):
	semua_akun = Barang.objects.all()

	context = {
		'title' : 'List Barang',
		'semua_akun' : semua_akun,
	}

	return render(request, 'barang/list.html',context)

def create(request):
	akun_form = BarangForm(request.POST or None)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('barang:list')

	context = {
		'title' : 'Inputan Barang',
		'akun_form' : akun_form,
	}

	return render(request, 'barang/create.html', context)

def delete(request, delete_id):
	Barang.objects.filter(id=delete_id).delete()
	return redirect('barang:list')

def update(request, update_id):
	akun_update = Barang.objects.get(id=update_id)

	data = {
		'ID_Detail': akun_update.ID_Detail,
		'Kode_Barang': akun_update.Kode_Barang,
		'Nama_Barang': akun_update.Nama_Barang,
		'Merk': akun_update.Merk,
		'Stock': akun_update.Stock,
		'BAP_Kedatangan': akun_update.BAP_Kedatangan,		
	}
	akun_form = BarangForm(request.POST or None, initial=data, instance=akun_update)
	
	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('barang:list')

	context = {
		'title' : 'Update Barang',
		'akun_form' : akun_form,
	}

	return render(request, 'barang/create.html', context)