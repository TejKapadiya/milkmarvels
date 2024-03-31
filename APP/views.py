from django.shortcuts import render
import os
from django.db.models import Count
# from urllib3 import request
from django.http import HttpResponse 
from django.shortcuts import render
from django.views import View
from . models import Product
# Create your views here.
# def login(request):
#     return render(request,"home.html")

def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")


def cart(request):
    return render(request,"cart.html")


class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"category.html",locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"category.html",locals())


class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"productdetail.html",locals())