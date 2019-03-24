from django.shortcuts import render
from .models import Services

# Create your views here.
def services(request):
    servicios = Services.objects.all()
    return  render(request,"services/services.html",{'services':servicios})