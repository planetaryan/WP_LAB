# calculator/views.py
from django.shortcuts import render

def calculator_view(request):
    if request.method == "POST":
        # Logic to handle input and calculate result based on user inputs
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Cannot divide by zero'
        
        return render(request, 'calculator/index.html', {'result': result})
    
    return render(request, 'calculator/index.html')
