from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import User
from .models import *

def Index(request):
	return HttpResponse("Hola")

def ListUsuarios(request):
	users = User.objects.all()
	profiles = Profile.objects.all()
	context = {'users': users, 'profiles': profiles}
	return render(request, 'mantenedor/list_user.html', context)

def AddUsuarios(request):
	if request.method == 'POST':
		form =  UserCreateForm(request.POST)
		profile_form = ProfileForm(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user = form.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			return redirect('list_user')
	else:
		form =  UserCreateForm()
		profile_form = ProfileForm()
	context = {'form': form, 'profile_form': profile_form}
	return render(request, 'mantenedor/add_user.html', context)


def EditarUsuarios(request, id):
	profile = Profile.objects.get(id=id)
	user = User.objects.get(id=profile.user.id)
	if request.method == 'POST':
		form =  UserCreateForm(request.POST, instance=user)
		profile_form = ProfileForm(request.POST, instance=profile)
		if form.is_valid() and profile_form.is_valid():
			form.save()
			profile_form.save()
			return redirect('list_user')
		else:
			return render(request, 'mantenedor/edit_user.html', {'form': form, 'profile_form': profile_form})
	else:
		form =  UserCreateForm(instance=user)
		profile_form = ProfileForm(instance=profile)
		context = {'form': form, 'profile_form': profile_form}
		return render(request, 'mantenedor/edit_user.html', context)

def EliminarUsuarios(request, id):
	profile = Profile.objects.get(id=id)
	if request.method == 'POST':
		profile.delete()
		return redirect('list_user')
	else:
		return render(request, 'mantenedor/delete_user.html', {'profile': profile})