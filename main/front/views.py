from django.shortcuts import render, redirect
from main import models

def index(request):
    products = models.Product.objects.all()
    context = {
        'products':products
    }
    return render(request,"front/index.html",context)