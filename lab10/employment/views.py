from django.shortcuts import render, redirect
from .forms import WorksForm, LivesForm
from .models import Works, Lives
from django.db.models import Q

# View for inserting data into the WORKS table
def add_works(request):
    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_works')
    else:
        form = WorksForm()
    return render(request, 'employment/add_works.html', {'form': form})

# View for inserting data into the LIVES table
def add_lives(request):
    if request.method == 'POST':
        form = LivesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_lives')
    else:
        form = LivesForm()
    return render(request, 'employment/add_lives.html', {'form': form})

# View to retrieve people working at a particular company and the cities they live in
def people_in_company(request):
    people = []
    company_name = ''
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        people = Works.objects.filter(company_name=company_name)
        people = [(person.person_name, person.company_name, 
                   Lives.objects.filter(person_name=person.person_name).first().city) for person in people]
    return render(request, 'employment/people_in_company.html', {'people': people, 'company_name': company_name})
