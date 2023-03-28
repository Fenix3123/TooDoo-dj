from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import toodoo
from .forms import toodooform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here. HttpResponse("hello world")


@login_required(login_url='loginRegistration')
def get_dashboard(request):
    current_user = request.user
    TooDoo = toodoo.objects.filter(user = current_user)
    context = {'toodoo' : TooDoo, 'user' : current_user}
    return render(request, 'dashboard.html', context)

@login_required(login_url='loginRegistration')
def createTooDoo(request):
    form = toodooform()
    #form in toodoo_form.html gets saved here
    if request.method == "POST":
        print(request.POST)
        form = toodooform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
            
    context = {'form': form}
    return render(request, 'toodoo_form.html', context)

#go to 58:56 you need to look into dynamic values for this
@login_required(login_url='loginRegistration')
def updateTooDoo(request, pk):
    toodooobj = toodoo.objects.get(id=pk)
    form = toodooform(instance=toodooobj)
    if request.method == 'POST':
        form = toodooform(request.POST, instance=toodooobj)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {'form' : form, 'toodoo': toodooobj}
    return render(request, 'toodooinfo.html', context)
@login_required(login_url='loginRegistration')
def deleteTooDoo(request, pk):
    toodooobj = toodoo.objects.get(id=pk)
    if request.method == 'POST':
        toodooobj.delete()
    return redirect('dashboard')

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')
            
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username OR password does not exist')
            
    context = {'page':page}
    return render(request, 'loginRegistration.html', context)

def registerUser(request):
    form = UserCreationForm
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'An error occured during registration')
    return render(request, 'loginRegistration.html', {'form':form})
    
def logoutUser(request):
    logout(request)
    return redirect('dashboard')