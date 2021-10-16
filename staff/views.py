from django.shortcuts import render, redirect

# Create your views here.
from .models import Pegawai
from .forms import PegawaiForm

def list(request):
	semua_akun = Pegawai.objects.all()

	context = {
		'title' : 'User',
		'semua_akun' : semua_akun,
	}

	return render(request, 'staff/list.html',context)

def create(request):
	akun_form = PegawaiForm(request.POST or None)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('staff:list')

	context = {
		'title' : 'Registrasi',
		'akun_form' : akun_form,
	}

	return render(request, 'staff/create.html', context)

def delete(request, delete_id):
	Pegawai.objects.filter(id=delete_id).delete()
	return redirect('staff:list')

def update(request, update_id):
	akun_update = Pegawai.objects.get(id=update_id)

	data = {
		'NIP_NRK' : akun_update.NIP_NRK,
		'nama_depan' : akun_update.nama_depan,
		'nama_belakang' : akun_update.nama_belakang,
		'Alamat' : akun_update.Alamat,
		'Email' : akun_update.Email,
		'Telp' : akun_update.Telp,
		'Role' : akun_update.Role,
	}
	akun_form = PegawaiForm(request.POST or None, initial=data, instance=akun_update)
	
	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('staff:list')

	context = {
		'title' : 'Update Akun',
		'akun_form' : akun_form,
	}

	return render(request, 'staff/create.html', context)