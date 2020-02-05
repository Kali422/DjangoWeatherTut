from django.shortcuts import render

# Create your views here.
# This is views

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})