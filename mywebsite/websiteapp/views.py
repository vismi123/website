from urllib import request

from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.

# def myweb(request):
#     return HttpResponse("hello i am inmakes")
# def about(request):
#           return render(request,"index.html")
# def about(request):
#     return render(request,"contact.html")
# def details(request):
#     return render(request,"details.html")
# def thanku(request):
#     return render(request,"thanku.html")
from django.shortcuts import render


def index(request):
    return render(request,"index.html")


def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])

        addition_result = num1 + num2
        subtraction_result = num1 - num2
        multiplication_result = num1 * num2

        if num2 != 0:
            division_result = num1 / num2
        else:
            division_result = 'Cannot divide by zero'

        return render(request, "result.html", {
            'addition_result': addition_result,
            'subtraction_result': subtraction_result,
            'multiplication_result': multiplication_result,
            'division_result': division_result
        })

    return HttpResponse("Method not allowed")