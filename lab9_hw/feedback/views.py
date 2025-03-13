# feedback/views.py
from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    message = None
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Get data from the form
            student_name = form.cleaned_data['student_name']
            sex = form.cleaned_data['sex']
            
            # Generate message based on name and sex
            if sex == 'Male':
                message = f"Thanks Mr. {student_name} for your feedback."
            else:
                message = f"Thanks Miss. {student_name} for your feedback."
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback_form.html', {'form': form, 'message': message})
