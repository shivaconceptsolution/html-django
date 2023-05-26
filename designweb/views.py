from django.shortcuts import render,redirect
from .models import Registration
from django.http import HttpResponse
def index(request):
    if request.method=="POST":
        obj = Registration(username=request.POST["txtuser"],password=request.POST["txtpass"],email=request.POST["txtemail"],mobile=request.POST["txtmobile"])
        obj.save()
        return render(request,"designweb/index.html",{"key":"Inserted Successfully"})
    return render(request,"designweb/index.html")
def about(request):
    return render(request,"designweb/about.html")
def services(request):
    return render(request,"designweb/services.html")
def gallery(request):
    return render(request,"designweb/gallery.html")
def contacts(request):
    return render(request,"designweb/contact.html")
def login(request):
    if request.method=="POST":
        res= Registration.objects.filter(username=request.POST["txtuser"],password=request.POST["txtpass"]);
        if(res.count()>0):
            return redirect('profile')
        else:
            return render(request,"designweb/login.html",{"res":'invalid userid and password'})    
    return render(request,"designweb/login.html")    
def profile(request):
    obj = Registration.objects.all()
    return render(request,"designweb/dashboard/profile.html",{'res':obj})
def editprofile(request):
    return HttpResponse("Edit")

def deleteprofile(request):
    return HttpResponse("Delete")