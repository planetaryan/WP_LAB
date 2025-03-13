# billing/views.py
from django.shortcuts import render, redirect
from .forms import BillingForm

# Prices of the different mobile brands and categories
PRICES = {
    'HP': 500,
    'Nokia': 300,
    'Samsung': 800,
    'Motorola': 600,
    'Apple': 1000,
}

def billing(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            # Get form data
            item = form.cleaned_data['item']
            categories = form.cleaned_data['categories']
            quantity = form.cleaned_data['quantity']
            
            # Calculate total bill
            price = PRICES.get(item, 0)
            total = price * quantity
            
            # Store data in session
            request.session['item'] = item
            request.session['categories'] = ', '.join(categories)
            request.session['quantity'] = quantity
            request.session['total'] = total

            # Redirect to result page
            return redirect('bill_summary')
    else:
        form = BillingForm()

    return render(request, 'billing/billing_form.html', {'form': form})

def bill_summary(request):
    # Retrieve data from session
    item = request.session.get('item', 'N/A')
    categories = request.session.get('categories', 'N/A')
    quantity = request.session.get('quantity', 0)
    total = request.session.get('total', 0)

    return render(request, 'billing/bill_summary.html', {
        'item': item,
        'categories': categories,
        'quantity': quantity,
        'total': total
    })
