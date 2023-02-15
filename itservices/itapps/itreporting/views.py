from django.shortcuts import render
from .models import Issue

# Create your views here.
def home(request):
    return render(request, 'itreporting/home.html')

def about(request):
    return render(request, 'itreporting/about.html',  {'title': 'About Us'})

def report(request):
    daily_report = {
        'issues': Issue.objects.all()
    }

    return render(request, 'itreporting/report.html', daily_report)

def contact(request):
    return render(request, 'itreporting/contact.html')