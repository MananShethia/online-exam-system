from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def support(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    return render(request, 'signup.html')