from django.shortcuts import render,redirect
from laModa.models import category_db,product_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from NewApp.models import contact_db
from django.contrib import messages
# Create your views here.
def index_page(req):
    return render(req,"index.html")

def add_category(req):
    return render(req,"add_category.html")

def save_category(request):
    if request.method=="POST":
        cn=request.POST.get('CategoryName')
        des=request.POST.get('Description')
        img=request.FILES['Imageupload']
        obj=category_db(CategoryName=cn,Description=des,Imageupload=img)
        obj.save()
        messages.success(request,"category saved successfully..")
        return redirect(add_category)

def display_category(request):
    data=category_db.objects.all()
    return render(request,"display_category.html",{'data':data})
def edit_category(request,cat_id):
    data=category_db.objects.get(id=cat_id)
    return render(request,"edit_category.html",{'data':data})

def update_category(request,cat_id):
    if request.method=="POST":
        catn=request.POST.get('CategoryName')
        desc=request.POST.get('Description')
        try:
            img=request.FILES['Imageupload']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=category_db.objects.get(id=cat_id).Imageupload
        category_db.objects.filter(id=cat_id).update(CategoryName=catn,Description=desc,Imageupload=file)
        return redirect(display_category)

def delete_category(request,cat_id):
    x=category_db.objects.filter(id=cat_id)
    x.delete()
    messages.error(request,"deleted..")
    return redirect(display_category)

def admin_page(req):
    return render(req,"admin_login.html")

def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request,"welcome..")
                return redirect(index_page)
            else:
                messages.error(request,"invalid password..")
                return redirect(admin_page)

        else:
            messages.warning(request, "user not found.....")
            return redirect(admin_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_page)

def add_products(req):
    data=category_db.objects.all()
    return render(req,"add_products.html",{'data':data})
def save_products(req):
    if req.method=="POST":
        pn=req.POST.get('ProductName')
        pc=req.POST.get('ProductCategory')
        desc=req.POST.get('description')
        pri=req.POST.get('Price')
        img=req.FILES['ProductImage']
        obj=product_db(ProductName=pn,ProductCategory=pc,description=desc,Price=pri,ProductImage=img)
        obj.save()
        return redirect(add_products)

def display_products(req):
    data=product_db.objects.all()
    return render(req,"display_products.html",{'data':data})

def edit_products(request,prod_id):
    prod=product_db.objects.get(id=prod_id)
    cat=category_db.objects.all()
    return render(request,"edit_products.html",{'prod':prod,'cat':cat})

def update_products(request,prod_id):
    if request.method=="POST":
        pname=request.POST.get('ProductName')
        pcat=request.POST.get('ProductCategory')
        descr=request.POST.get('description')
        pric=request.POST.get('Price')
        try:
            img=request.FILES['ProductImage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=product_db.objects.get(id=prod_id).ProductImage
        product_db.objects.filter(id=prod_id).update(ProductName=pname,ProductCategory=pcat,description=descr,Price=pric,ProductImage=file)
        return redirect(display_products)

def delete_products(request,prod_id):
    x=product_db.objects.filter(id=prod_id)
    x.delete()
    return redirect(display_products)

def contact_details(req):
    data=contact_db.objects.all()
    return render(req,"contact_data.html",{'data':data})
def contact_delete(req,cont_id):
    x=contact_db.objects.filter(id=cont_id)
    x.delete()
    return redirect(contact_details)


