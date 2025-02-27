# session_example/views.py
from django.shortcuts import render, redirect

def first_page(request):
    if request.method == 'POST':
        # Save data in session
        request.session['name'] = request.POST.get('name')
        request.session['roll'] = request.POST.get('roll')
        request.session['subject'] = request.POST.get('subject')
        
        # Redirect to second page
        return redirect('session_example:second_page')
    
    return render(request, 'session_example/firstPage.html')

def second_page(request):
    name = request.session.get('name', '')
    roll = request.session.get('roll', '')
    subject = request.session.get('subject', '')
    
    return render(request, 'session_example/secondPage.html', {
        'name': name,
        'roll': roll,
        'subject': subject,
    })
