from django.shortcuts import render,redirect
from .models import *
from .form import *

def create(request):
    a = studentForm()
    b = register.objects.all()         
    if request.method=='POST':
        a = studentForm(request.POST)
        if a.is_valid():
            a.save()
        else:print('Invalid Input')
    else:
        a = studentForm()   
    return render(request,'index.html',{'form':a,'data':b})

# def read(request):
#    b = register.objects.all()
#     return render(request,'read.html',{'data':b})

def edit(request,id):
    c = register.objects.get(id=id)
    d = register.objects.all()
    e = studentForm(instance=c)
    if request.method == 'POST':
         a = studentForm(request.POST,instance=c)
         if a.is_valid():
            a.save()
            return redirect('create')
         else:
             a = studentForm()
    else:
         a = studentForm()

    return render(request,'update.html',{'form':e,'data':d})
        
def delete(request,id):
    c= register.objects.get(id=id)
    c.delete()
    return redirect('create')

# Create your views here.
