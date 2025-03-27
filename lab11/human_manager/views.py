# human_manager/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Human
from .forms import HumanForm

def human_manager(request):
    humans = Human.objects.all()
    
    selected_human = None
    form = HumanForm()
    
    if request.method == 'POST':
        if 'update' in request.POST:
            human_id = request.POST.get('human_id')
            human = get_object_or_404(Human, id=human_id)
            form = HumanForm(request.POST, instance=human)
            if form.is_valid():
                form.save()
                return redirect('human_manager')
        
        elif 'delete' in request.POST:
            human_id = request.POST.get('human_id')
            human = get_object_or_404(Human, id=human_id)
            human.delete()
            return redirect('human_manager')
        
        elif 'human_id' in request.POST:
            human_id = request.POST.get('human_id')
            if human_id:
                selected_human = get_object_or_404(Human, id=human_id)
                form = HumanForm(instance=selected_human)
    
    return render(request, 'human_manager/index.html', {
        'humans': humans,
        'form': form,
        'selected_human': selected_human
    })