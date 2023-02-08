from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'itreporting/home.html')

def about(request):
    return render(request, 'itreporting/about.html',  {'title': 'About Us'})

def report(request):
    return render(request, 'itreporting/report.html')

def contact(request):
    return render(request, 'itreporting/contact.html')