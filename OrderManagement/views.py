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

def delete_customers(request,id):
    selected_customer=customers.objects.get(id=id)
    selected_customer.delete()
    return redirect('/order_management/view_customers/')

def update_customers(request, id):
    selected_customer=customers.objects.get(id=id)
    
    if request.method == 'POST':
        form=customer_form(request.POST, instance=selected_customer)
        if form.is_valid():
            form.save()
            return redirect('/order_management/view_customers/')
    else:
        form=customer_form(instance=selected_customer)

    context={
        'customer_form':form
    }

    return render(request,'add_customers.html',context)

def add_orders(request):

    if request.method =='POST':
        quantity_value=request.POST['quantity']
        selected_product=products.objects.get(id=request.POST['product'])


        amount = float(quantity_value) * float(selected_product.price)
        gst_amount= (amount * selected_product.gst)/100
        total_price=amount+gst_amount


        new_order=orders(
            customer_id=request.POST['customer'],
            product_id=request.POST['product'],
            order_number=request.POST['order_number'],
            order_date=request.POST['order_date'],
            quantity=quantity_value,
            amount=amount,
            gst_amount=gst_amount,
            total_price=total_price
        )

        new_order.save()

    context={
        'order_form':order_form()
        }

    return render(request,'add_orders.html',context)

def view_orders(request):

    selected_orders=orders.objects.all()

    context={
        'all_orders':selected_orders
    }

    return render(request,'orders.html',context)

def delete_orders(request,id):
    selected_order=orders.objects.get(id=id)
    selected_order.delete()
    return redirect('/order_management/view_orders/')

def update_orders(request,id):
    selected_order=orders.objects.get(id=id)
    if request.method == 'POST':
        quantity_value=request.POST['quantity']
        selected_product=products.objects.get(id=request.POST['product'])

        amount = float(quantity_value) * float(selected_product.price)
        gst_amount= (amount * selected_product.gst)/100
        total_price=amount+gst_amount

        filtered_order=orders.objects.filter(id=id)
        filtered_order.update(
            customer_id=request.POST['customer'],
            product_id=request.POST['product'],
            order_number=request.POST['order_number'],
            order_date=request.POST['order_date'],
            quantity=quantity_value,
            amount=amount,
            gst_amount=gst_amount,
            total_price=total_price
        )
        return redirect('/order_management/view_orders/')

    context={
        'order_form':order_form(instance=selected_order)
    }    

    return render(request,'add_orders.html',context)