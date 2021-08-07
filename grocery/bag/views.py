from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, GroceForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.
@login_required(login_url='login')
def home(request):
    groces = Groce.objects.all()

    context = {'groces':groces}

    return render(request, 'bag/dashboard.html', context)


def reg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'bag/reg.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'bag/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def addpage(request,):
    form = GroceForm()
    if request.method == 'POST':
        form = GroceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'bag/add.html', context)

@login_required(login_url='login')
def updateGroce(request, Groce_id):
    
    item = Groce.objects.get(pk=Groce_id)
    form = GroceForm(instance=item)

    if request.method == 'POST':
        form = GroceForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request, 'bag/add.html', context)

@login_required(login_url='login')
def DeleteGroce(request, Groce_id):
    
    item = Groce.objects.get(pk=Groce_id)
    item.delete()
    return redirect('home')