from django.shortcuts import render

book_info = {
    'title': 'The Great Gatsby',
    'author': 'F. Scott Fitzgerald',
    'cover_image': '/home/student/Downloads/bookcover.jpeg',  # Use a real path here or database if storing
    'metadata': 'Published in 1925, The Great Gatsby is widely regarded as one of the greatest American novels.',
    'reviews': 'The Great Gatsby is an extraordinary work, examining the American Dream.',
    'publisher_info': 'Scribner is the publisher of The Great Gatsby, a division of Simon & Schuster.'
}

def home(request):
    return render(request, 'book/home.html', {'book': book_info})

def metadata(request):
    return render(request, 'book/metadata.html', {'book': book_info})

def reviews(request):
    return render(request, 'book/reviews.html', {'book': book_info})

def publisher_info(request):
    return render(request, 'book/publisher_info.html', {'book': book_info})