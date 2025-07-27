from django.shortcuts import render, redirect
from .forms import *
from django.views import View

# Create your views here.
def home(request):
    return render(request, 'home.html')


'''def add_products(request):
    context = {
        'product_form': product_form(),
    }
    if request.method == 'POST':
        form= product_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventory/add_products/')
    return render(request, 'add_products.html',context) ''' 
'''def view_products(request):
    selected_products = products.objects.all()
    context={
        'products': selected_products,
    }

    return render(request, 'products.html',context)
'''
'''def delete_product(request,id):
    selected_product=products.objects.get(id=id)
    selected_product.delete()
    return redirect('/inventory/view_products/')
'''
'''def update_product(request,id):
    selected_product=products.objects.get(id=id)
    
    if request.method == 'POST':
        form=product_form(request.POST, instance=selected_product)
        if form.is_valid():
            form.save()
            return redirect('/inventory/view_products/')
    else:
        form=product_form(instance=selected_product)

    Context={
        'product_form':form
    }

    return render(request,'add_products.html',Context)
'''

class add_product_view(View):

    def get(self,request):
        context = {
        'product_form': product_form(),
        }
        return render(request, 'add_products.html',context)


    def post(self,request):
        form= product_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventory/view_products/')


class view_product_view(View):

    def get(self,request):
        selected_products = products.objects.all()
        context={
            'products': selected_products,
        }

        return render(request, 'products.html',context)
    

class delete_product_view(View):

    def get(self,request,id):
        selected_product=products.objects.get(id=id)
        selected_product.delete()
        return redirect('/inventory/view_products/')


class update_product_view(View):

    

    def get(self,request,id):

        selected_product=products.objects.get(id=id)
        
        form=product_form(instance=selected_product)
        Context={
            'product_form':form
        }

        return render(request,'add_products.html',Context)

    def post(self,request,id):

        selected_product=products.objects.get(id=id)
        
        form=product_form(request.POST, instance=selected_product)
        if form.is_valid():
            form.save()
            return redirect('/inventory/view_products/')
        
        Context={
            'product_form':form
        }

        return render(request,'add_products.html',Context)