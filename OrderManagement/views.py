from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def add_customers(request):
    
    if request.method == 'POST':
        form=customer_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/order_management/add_customers/')
    else:
        form=customer_form()

    context={
        'customer_form':form
    }
    return render(request, 'add_customers.html', context)

def view_customers(request):
   selected_customers=customers.objects.all()
   context={
       'all_customers': selected_customers
   }
   return render(request,'customers.html',context)
