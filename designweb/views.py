from django.shortcuts import render
from .models import Registration
def index(request):
    if request.method=="POST":
        obj = Registration(username=request.POST["txtuser"],password=request.POST["txtpass"],email=request.POST["txtemail"],mobile=request.POST["txtmobile"])
        obj.save()
        return render(request,"designweb/index.html",{"key":"Inserted Successfully"})
    return render(request,"designweb/index.html")
def about(request):
    obj = Registration.objects.all()
    return render(request,"designweb/about.html",{'res':obj})
def services(request):
    return render(request,"designweb/services.html")
def gallery(request):
    return render(request,"designweb/gallery.html")
def contacts(request):
    return render(request,"designweb/contact.html")