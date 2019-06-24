from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request,'home.html')

def home_copy(request):
    return render(request,'homecopy.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def carouselpage(request):
    return render(request,'carouselpage.html')