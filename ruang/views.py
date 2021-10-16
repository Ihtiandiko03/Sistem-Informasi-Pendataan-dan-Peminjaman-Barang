from django.shortcuts import render, redirect

# Create your views here.
from .models import Ruang
from .forms import RuangForm

def list(request):
	semua_akun = Ruang.objects.all()

	context = {
		'title' : 'List Ruang',
		'semua_akun' : semua_akun,
	}

	return render(request, 'ruang/list.html',context)

def create(request):
	akun_form = RuangForm(request.POST or None)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('ruang:list')

	context = {
		'title' : 'Create Ruang',
		'akun_form' : akun_form,
	}

	return render(request, 'ruang/create.html', context)

def delete(request, delete_id):
	Ruang.objects.filter(id=delete_id).delete()
	return redirect('ruang:list')

def update(request, update_id):
	akun_update = Ruang.objects.get(id=update_id)

	data = {
		'ID_Ruang' : akun_update.ID_Ruang,
		'Ruangan' : akun_update.Ruangan,
		'PJ_Ruang' : akun_update.PJ_Ruang,
		'Gedung' : akun_update.Gedung,
	}
	akun_form = RuangForm(request.POST or None, initial=data, instance=akun_update)
	
	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('ruang:list')

	context = {
		'title' : 'Update Ruang',
		'akun_form' : akun_form,
	}

	return render(request, 'ruang/create.html', context)