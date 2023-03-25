from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import toodoo
from .forms import toodooform
# Create your views here. HttpResponse("hello world")


def get_dashboard(request):
    TooDoo = toodoo.objects.all()
    context = {'toodoo' : TooDoo}
    return render(request, 'dashboard.html', context)

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

def deleteTooDoo(request, pk):
    toodooobj = toodoo.objects.get(id=pk)
    if request.method == 'POST':
        toodooobj.delete()
    return redirect('dashboard')