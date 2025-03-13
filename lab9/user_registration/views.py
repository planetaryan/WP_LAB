# user_registration/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            contact_number = form.cleaned_data.get('contact_number')
            # Redirect with parameters in the URL
            return redirect('success', username=username, email=email, contact_number=contact_number)
    else:
        form = RegistrationForm()

    return render(request, 'user_registration/register.html', {'form': form})

def success(request, username, email, contact_number):
    return render(request, 'user_registration/success.html', {
        'username': username,
        'email': email,
        'contact_number': contact_number
    })
