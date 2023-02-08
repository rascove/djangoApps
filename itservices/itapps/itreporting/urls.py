from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='itreporting-home'),
    path('about', views.about, name='itreporting-about'),
    path('report', views.report, name='itreporting-report'),
    path('contact', views.contact, name='itreporting-contact'),
]