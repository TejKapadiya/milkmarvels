from django.shortcuts import render,redirect
import os
from django.db.models import Count
# from urllib3 import request
from django.http import HttpResponse ,JsonResponse
from django.shortcuts import render
from django.views import View
from . models import Product , Customer ,Cart ,OrderPlaced
# from django.contrib.auth.forms import MySetPasswordForm

from . forms import CustomerRegistrationForm , CustomerProfileForm ,MySetPasswordForm
from django.contrib import messages
from django.db.models import Q
# from django.contrib.auth.decorators import login_required



def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")


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
        form = CustomerRegistrationForm()  
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
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render (request,'updateaddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success (request, "Congratulations! Profile Update Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect("address")



def add_to_cart(request):
    user =  request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user , product=product).save()
    return redirect('/cart')


def show_cart(request):
    user =  request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
        totalamount = amount + 40
    return render(request,'addtocart.html',locals())


class checkout(View):
    def get(self,request):
        user=request.user
        add=Customer.objects.filter (user=user)
        cart_items=Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 40
        return render(request,'checkout.html',locals())



def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        #print(prod_id)
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity* p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data={
        'quantity':c.quantity,
        'amount': amount,
        'totalamount': totalamount
        }
        return JsonResponse(data)



def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        print(c.quantity)
        c.save()
        user = request.user
        cart = Cart.objects.filter (user=user)
        amount = 0
        
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        data={
        'quantity':c.quantity,
        'amount': amount,
        'totalamount': totalamount
        }
        
        return JsonResponse (data)



def remove_cart (request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        user = request.user
        c.delete()

        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount 
        data={
        'amount': amount,
        'totalamount': totalamount
        }

        return redirect('/cart')


def orders(request):
    order_placed = OrderPlaced.objects.filter(user=request.user) 
    return render(request, 'order.html ',locals())



from django.shortcuts import redirect, render
from django.contrib import messages

from .models import Cart, Product, Customer, OrderPlaced, Payment

def paynow(request):
    if request.method == 'POST':
        # Get the selected shipping address ID from the form
        address_id = request.POST.get('custid')
        print(address_id)
        # Get the user's cart items
        cart_items = Cart.objects.filter(user=request.user)
        print(cart_items)

        if address_id:

            try:

                # Get the selected shipping address using the address_id
                address = Customer.objects.get(pk=address_id)  # Assuming address is stored within Customer model
            except Customer.DoesNotExist:

                messages.error(request, 'Invalid shipping address.')
                return redirect('checkout')

            # Create a single Payment object for the entire order
            payment = Payment.objects.create(user=request.user, amount=0)  # Payment amount will be calculated later

            for cart_item in cart_items:
                # Create an OrderPlaced object for each cart item
                order = OrderPlaced.objects.create(
                    user=request.user,
                    address=address,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    status='Accepted',
                    payment=payment,
                )

                # Update payment amount to reflect total cost of all items
                payment.amount += order.total_cost

            # Save the final payment amount
            payment.save()

            # Clear the user's cart after placing the order
            Cart.objects.filter(user=request.user).delete()

            # Redirect to a success page or any other page after placing the order
            return redirect(orders)

        else:
            messages.error(request, 'Please select a shipping address.')
            return redirect('checkout')

    else:
        # Handle GET request (display the checkout page)
        # Your existing code for rendering the checkout page goes here
        return render(request, 'TEST.html')



def search(request):
    query = request.GET['search']
    totalitem=0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, "search.html", locals())