from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

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