# cgpa_calculator/views.py
from django.shortcuts import render, redirect
from .forms import CGPAForm

def calculate(request):
    if request.method == 'POST':
        form = CGPAForm(request.POST)
        if form.is_valid():
            # Get data from the form
            name = form.cleaned_data['name']
            total_marks = form.cleaned_data['total_marks']

            # Store the data in session
            request.session['name'] = name
            request.session['total_marks'] = total_marks

            return redirect('result')
    else:
        form = CGPAForm()

    return render(request, 'cgpa_calculator/form.html', {'form': form})

def result(request):
    # Get the data from session
    name = request.session.get('name')
    total_marks = request.session.get('total_marks')

    # Calculate CGPA (total_marks / 50)
    if total_marks is not None:
        cgpa = total_marks / 50
    else:
        cgpa = 0

    return render(request, 'cgpa_calculator/result.html', {'name': name, 'cgpa': cgpa})
