from django.shortcuts import render
from .models import Institute

# View to display a list of institute names in a list box
def institute_list(request):
    institutes = Institute.objects.all()  # Fetch all institutes
    return render(request, 'institutes/institute_list.html', {'institutes': institutes})
