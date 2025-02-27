# carinfo/views.py
from django.shortcuts import render

def index(request):
    # List of car manufacturers for dropdown
    car_manufacturers = ['Toyota', 'Ford', 'BMW', 'Tesla', 'Honda']
    return render(request, 'carinfo/index.html', {'car_manufacturers': car_manufacturers})

def result(request):
    if request.method == "GET":
        manufacturer = request.GET.get('manufacturer')
        model = request.GET.get('model')
        return render(request, 'carinfo/result.html', {'manufacturer': manufacturer, 'model': model})
