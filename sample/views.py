from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactpage.html')


def login(request):
    return render(request, 'loginpage.html')
