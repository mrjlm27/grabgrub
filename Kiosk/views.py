from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from .models import Food,Customer,Order,OrderLine
from .forms import CustomerForm, FoodForm, OrderLineForm,OrderForm
# Create your views here.

def homepage(request):
    return render(request,'Kiosk/home.html')

def customerlist(request):
    customer_objects = Customer.objects.all()
    return render(request,'Kiosk/CUSTOMER/customer_list.html',{'customers':customer_objects})

def foodlist(request):
    food_objects=Food.objects.all()
    return render(request,'Kiosk/FOOD/food_list.html',{'foods':food_objects}) 

def customerorder(request,pk):
    customer = OrderLine.objects.filter(ORD__cust_order__pk=pk)
    cust_order = Customer.objects.get(pk=pk)
    c_obj = get_object_or_404(Customer, pk=pk)
    gtotal = sum( d.solver() for d in OrderLine.objects.filter(ORD__cust_order__name = cust_order.name))
    return render(request,'Kiosk/CUSTOMER/customerorder.html',{'customer':customer,'c_obj':c_obj,'gtotal':gtotal,'cust_order':cust_order})


def vieworders(request):
    orderline_objects=OrderLine.objects.all()
    return render(request,'Kiosk/ORDER/order_list.html',{'orderline_objects':orderline_objects,})


def addordersform(request):
    customer_objects=Customer.objects.all()
    food_objects=Food.objects.all()
    if(request.method=='POST'):
        nCustomerOrder = request.POST.get('CustomerName')
        nPayment = request.POST.get('PaymentType')
        nFood = request.POST.get('food')
        nQuant = request.POST.get('quantity')
        nOrder = Order.objects.create(cust_order=Customer.objects.get(pk=nCustomerOrder),mode_payment= nPayment)
        OrderLine.objects.create(ORD=nOrder,food=Food.objects.get(pk=nFood),quantity=nQuant)
        return redirect('vieworders')
    else:
        return render(request,'Kiosk/ORDER/addorder.html',{'c':customer_objects,'f':food_objects})

def deleteorder(request,pk):
    Order.objects.filter(pk=pk).delete()
    OrderLine.objects.filter(pk=pk).delete()
    return redirect('vieworders')

def editordersform(request,pk):
    customer_objects=Customer.objects.all()
    food_objects = Food.objects.all()
    order_objects = Order.objects.all()
    if(request.method=='POST'):
        nPayment = request.POST.get('PaymentType')
        nFood = request.POST.get('food')
        nQuantity = request.POST.get('quantity')
        Order.objects.filter(pk=pk).update(mode_payment=nPayment)
        OrderLine.objects.filter(pk=pk).update(ORD=Order.objects.get(pk=pk),food=Food.objects.get(pk=nFood),quantity=nQuantity)
        return redirect('vieworders')
    else:
        o = get_object_or_404(OrderLine,pk=pk)
        return render(request, 'Kiosk/ORDER/editorder.html',{'o':o,'c':customer_objects,'f':food_objects, 'Order':order_objects})

def customerform(request,id=0):
    if request.method == "GET":
        if id==0:
            customer_form = CustomerForm()
        else:
            customer = Customer.objects.get(pk=id)
            customer_form = CustomerForm(instance=customer)
        return render(request,'Kiosk/CUSTOMER/addcustomer.html',{'cform':customer_form})
    else:
        if id==0:
            customer_form = CustomerForm(request.POST)
        else:            
            customer = Customer.objects.get(pk=id)
            customer_form = CustomerForm(request.POST,instance=customer)
        if customer_form.is_valid():
            customer_form.save()
        return redirect('/grabgrub/viewcustomers.html')

def foodform(request,id=0):
    if request.method == "GET":
        if id==0:
            food_form = FoodForm()
        else:
            food = Food.objects.get(pk=id)
            food_form = FoodForm(instance=food)
        return render(request,'Kiosk/FOOD/addfood.html',{'fform':food_form})
    else:
        if id==0:
            food_form = FoodForm(request.POST)
        else:            
            food = Food.objects.get(pk=id)
            food_form = FoodForm(request.POST,instance=food)
        if food_form.is_valid():
            food_form.save()
        return redirect('/grabgrub/viewfood.html')