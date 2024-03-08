from django.shortcuts import render
import os
# Create your views here.
# def login(request):
#     return render(request,"home.html")

def home(request):
    return render(request,"home.html")


def cart(request):
    return render(request,"cart.html")