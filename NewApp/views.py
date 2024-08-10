from django.shortcuts import render,redirect
from laModa.models import product_db,category_db
from NewApp.models import contact_db,register_db,cart_db,placeorder_db
from django.contrib import messages
import razorpay
# Create your views here.
def home_page(req):
    cat=category_db.objects.all()
    return render(req,"home.html",{'cat':cat})
def about_page(req):
    cat = category_db.objects.all()
    return render(req,"about.html",{'cat':cat})
def contact_page(req):
    cat = category_db.objects.all()
    return render(req,"contact.html", {'cat': cat})

def save_contact(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        pho=req.POST.get('phone')
        sub=req.POST.get('subject')
        mess=req.POST.get('message')
        obj=contact_db(name=na,email=em,phone=pho,subject=sub,message=mess)
        obj.save()
        return redirect(contact_page)


def our_products(req):
    cat = category_db.objects.all()
    pro=product_db.objects.all()
    return render(req,"our_products.html",{'products':pro,'cat':cat})

def filtered_products(req,cat_name):
    cat = category_db.objects.all()
    data=product_db.objects.filter(ProductCategory=cat_name)
    return render(req,"products_filtered.html",{'data':data,'cat':cat})

def single_products(req,prod_id):
    data=product_db.objects.get(id=prod_id)
    return render(req,"single_product.html",{'data':data})

def register_page(req):
    return render(req,"register.html")

def save_register(req):
    if req.method=="POST":
        un=req.POST.get('username')
        em=req.POST.get('email')
        pwd=req.POST.get('password')
        cpwd=req.POST.get('confirm_password')
        obj=register_db(username=un,email=em,password=pwd,confirm_password=cpwd)
        if register_db.objects.filter(username=un).exists():
            messages.success(req, "username already exists..")
            return redirect(register_page)
        elif register_db.objects.filter(email=em).exists():
            messages.success(req, "email already exists..")
            return redirect(register_page)
        else:
            obj.save()
            messages.success(req, "registered successfully..")
        return redirect(register_page)

def userlogin(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pwd=request.POST.get('password')
        if register_db.objects.filter(username=un,password=pwd).exists():
            request.session['username']=un
            request.session['password']=pwd
            messages.success(request, "login succesfully..")
            return redirect(home_page)
        else:
            messages.warning(request,"invalid username or password..")
            return redirect(register_page)
    else:
        return redirect(register_page)

def userlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "logoout succesfully..")
    return redirect(home_page)

def cart_page(request):
    #['username'] is from above userlogin 's username
    data=cart_db.objects.filter(username=request.session['username'])
    subtotal=0
    shipping_charge=0
    total=0
    for d in data:
        subtotal=subtotal+d.total_price
        if subtotal>500:
            shipping_charge=50
        else:
            shipping_charge=100
        total=shipping_charge+subtotal
    return render(request,"cart.html",{'data':data,'total':total,'shipping_charge':shipping_charge,'subtotal':subtotal})

def save_cart(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pn = request.POST.get('ProductName')
        qua = request.POST.get('quantity')
        tp = request.POST.get('total_price')
        obj = cart_db(username=un, ProductName=pn, quantity=qua, total_price=tp)
        obj.save()
        messages.success(request, "saved succesfully..")
        return redirect(home_page)

def delete_cart(request,p_id):
    x=cart_db.objects.filter(id=p_id)
    x.delete()
    messages.success(request, "deleted succesfully..")
    return redirect(cart_page)

def user_login_page(request):
    return render(request,"user_login.html")

def checkout_page(request):
    data=cart_db.objects.filter(username=request.session['username'])
    subtotal = 0
    shipping_charge = 0
    total = 0
    for d in data:
        subtotal = subtotal + d.total_price
        if subtotal > 500:
            shipping_charge = 50
        else:
            shipping_charge = 100
        total = shipping_charge + subtotal
    return render(request,"checkout.html",{'data':data,'subtotal':subtotal,'total':total,'shipping_charge':shipping_charge})

def payment_page(request):
    #retrieve the placeorder_db object with the specified id
    customer=placeorder_db.objects.order_by('-id').first()

    #Get the payment amount of the specified customer
    pay=customer.total_price

    #convert the amount to Paisa(smallest currency unit
    amount=int(pay*100)             #assuming payment amount in rupees

    #convert amount to string for printing
    pay_str=str(amount)

    #printing each character of the payment amount
    for i in pay_str:
        print(i)
    if request.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_VuEafQLHBKrSGH','vbTtWMTJU57Kcl8U7GP2bLa2'))
        payment=client.order.create({'amount':amount,'currency':order_currency,'payment_capture':'1'})
    return render(request,"payment.html",{'customer':customer,'pay_str':pay_str})


def save_placeorder(request):
    if request.method == "POST":
        na = request.POST.get('Name')
        em = request.POST.get('email')
        add = request.POST.get('Address')
        pho = request.POST.get('Phone')
        bill = request.POST.get('bill')
        tp = request.POST.get('total')
        obj = placeorder_db(Name=na,email=em,Address=add,phone=pho,bill=bill,total_price=tp)
        obj.save()
        return redirect(payment_page)
