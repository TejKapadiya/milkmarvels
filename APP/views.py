from django.shortcuts import render
import os
from django.db.models import Count
# from urllib3 import request
from django.http import HttpResponse 
from django.shortcuts import render
from django.views import View
from . models import Product , Customer
from . forms import CustomerRegistrationForm , CustomerProfileForm
from django.contrib import messages

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


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()  # Corrected form instantiation
        return render(request, "customerregistration.html", locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations!! Registered Successfully")
        else:
            messages.warning(request, "Invalid input!! Registration Failed")
        return render(request, "customerregistration.html", locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,"profile.html",locals())
        
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
        
            reg = Customer(user=user,name=name, locality=locality, mobile=mobile, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile Save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request,"profile.html",locals())


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,"address.html",locals())


class updateAddress(View):
    def get(self,request,pk):
        form = CustomerProfileForm()
        return render (request,'updateaddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm()
        return render (request,'updateaddress.html',locals())
