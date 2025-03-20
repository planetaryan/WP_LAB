from django.shortcuts import render, redirect
from .forms import CategoryForm, PageForm
from .models import Category, Page

# View to add a new category
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'directory/add_category.html', {'form': form})

# View to add a new page
def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_list')
    else:
        form = PageForm()
    return render(request, 'directory/add_page.html', {'form': form})

# View to list all categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'directory/category_list.html', {'categories': categories})

# View to list all pages
def page_list(request):
    pages = Page.objects.all()
    return render(request, 'directory/page_list.html', {'pages': pages})
