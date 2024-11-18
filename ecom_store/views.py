from django.shortcuts import get_object_or_404, render, redirect 
from .models import Orders 
from .forms import OrderForm

#Create your views here.

# Homepage
def home(request): 
    return render(request, 'ecom_store/homepage.html')

# Order list
def order_list(request): 
    orders = Orders.objects.all()
    return render(request, 'ecom_store/order_list.html', {'orders': orders})

# Create Order
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ecom_store:order_list')
    else:
        form = OrderForm()
    return render(request, 'ecom_store/order_form.html', {'form': form})

# Edit order
def order_edit(request, pk):
    order = get_object_or_404(Orders, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('ecom_store:order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'ecom_store/order_form.html', {'form': form})

# Delete order
def order_delete(request, pk):
    order = get_object_or_404(Orders, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect('ecom_store:order_list')
    return render(request, 'ecom_store/order_confirm_delete.html', {'order': order})