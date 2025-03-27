# product/views.py
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})