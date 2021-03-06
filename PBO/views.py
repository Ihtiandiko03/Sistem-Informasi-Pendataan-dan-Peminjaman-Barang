from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
	context = {
		'heading' : 'Inventaris Kampus',
		'content' : '',
	}

	template_name = None
	if request.user.is_authenticated():
		template_name = 'index_user.html'
	else:
		template_name = 'index_anonymous.html'
	return render(request, template_name, context)

def loginView(request):
	context = {
		'judul' : 'LOGIN',
	}

	user = None

	if request.method == "GET":
		if request.user.is_authenticated():
			return redirect('index')
		else:
			return render(request, 'login.html', context)

	if request.method == "POST":

		username_login = request.POST['username']
		password_login = request.POST['password']

		user = authenticate(request, username = username_login, password = password_login)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			return redirect('login')

@login_required
def logoutView(request):
	context = {
		'judul' : 'LogOut',
	}
	if request.method == "POST":
		if request.POST["logout"] == 'Submit':
			logout(request)

			return redirect('index')
	return render(request, 'logout.html',context)