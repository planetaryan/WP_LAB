# grocery_checklist/views.py
from django.shortcuts import render

def index(request):
    # List of grocery items with prices
    grocery_items = [
        {'name': 'Wheat', 'price': 40},
        {'name': 'Jaggery', 'price': 70},
        {'name': 'Dal', 'price': 80},

    ]

    # Handle form submission (POST request)
    if request.method == 'POST':
        selected_items = []
        for item in grocery_items:
            # If the checkbox for an item is checked (item.name is in POST data)
            if request.POST.get(item['name']):
                selected_items.append(item)
        
        return render(request, 'grocery_checklist/index.html', {
            'grocery_items': grocery_items,
            'selected_items': selected_items,
        })
    
    # For GET request, just render the form with all items
    return render(request, 'grocery_checklist/index.html', {
        'grocery_items': grocery_items,
        'selected_items': [],
    })
