from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.

def user_login(request):
    
    if request.method == 'POST':
        user=authenticate(request,username=request.POST["username"],password=request.POST["password"])
        if user is not None:
            login(request,user)
            return redirect('/inventory/home/')
        else:
            context={
                'error':"* Invalid username or password "
            }
            return render(request,'login.html',context)

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def user_register(request):
    if request.method == 'POST':

        if user.objects.filter(username=request.POST['username']).exists():
            context={
                'error':"username already exists"
            }
            return render(request,'register.html',context)
        
        else:

            if request.POST['password1']== request.POST['password2']:

                form=user.objects.create_user(username=request.POST['username'],
                                        first_name=request.POST['firstname'],
                                        last_name=request.POST['lastname'],
                                        email=request.POST['email'],
                                        age=request.POST['age'],
                                        password=request.POST['password1']
                                        )
                return redirect('/')
        


    return render(request,'register.html')