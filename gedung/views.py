from django.shortcuts import render, redirect

# Create your views here.
from .models import Gedung
from .forms import GedungForm

def list(request):
	semua_akun = Gedung.objects.all()

	context = {
		'title' : 'List Gedung',
		'semua_akun' : semua_akun,
	}

	return render(request, 'gedung/list.html',context)

def create(request):
	akun_form = GedungForm(request.POST or None)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('gedung:list')

	context = {
		'title' : 'Input Gedung',
		'akun_form' : akun_form,
	}

	return render(request, 'gedung/create.html', context)

def delete(request, delete_id):
	Gedung.objects.filter(id=delete_id).delete()
	return redirect('gedung:list')

def update(request, update_id):
	akun_update = Gedung.objects.get(id=update_id)

	data = {
		'ID_Gedung' : akun_update.ID_Gedung,
		'Nama_Gedung' : akun_update.Nama_Gedung,
		'PJ_Gedung' : akun_update.PJ_Gedung,
	}
	akun_form = GedungForm(request.POST or None, initial=data, instance=akun_update)
	
	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('gedung:list')

	context = {
		'title' : 'Update Gedung',
		'akun_form' : akun_form,
	}

	return render(request, 'gedung/create.html', context)