from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

from django.shortcuts import render

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')
def employee(request):
    emp=["varshi","kows","bismi"]
    return render(request,'emp.html',{"emps":emp})
def employees(request):
    details=[{"name": "Varshi", "jobtitle": "Developer", "salary": 50000,"worktime":"full-time"}, {"name": "Kows", "jobtitle": "Designer", "salary": 45000,"worktime":"part-time"}, {"name": "Bismi", "jobtitle": "Manager", "salary": 60000,"worktime":"full-time"}]
    return render(request, 'emp.html', {"detail": details})