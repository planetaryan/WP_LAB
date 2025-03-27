from django.shortcuts import render, redirect
from .forms import AuthorForm, PublisherForm, BookForm
from .models import Author, Publisher, Book

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_author')
    else:
        form = AuthorForm()
    return render(request, 'library/add_author.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_publisher')
    else:
        form = PublisherForm()
    return render(request, 'library/add_publisher.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'library/list_books.html', {'books': books})
