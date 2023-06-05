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
            request.session['uname']=request.POST["txtuser"]
            return redirect('profile')
        else:
            return render(request,"designweb/login.html",{"res":'invalid userid and password'})    
    return render(request,"designweb/login.html")    
def profile(request):
    if(request.session.has_key('uname')):
       obj = Registration.objects.filter(username=request.session['uname'])
       return render(request,"designweb/dashboard/profile.html",{'res':obj,'sessionkey':request.session['uname']})
    else:
        return redirect('/designweb/login')   
def editprofile(request):
    id = request.GET["q"]
    obj = Registration.objects.get(pk=id)
    if request.method=="POST":
        obj.username=request.POST["txtuname"]
        obj.password=request.POST["txtpass"]
        obj.email=request.POST["txtemail"]
        obj.mobile=request.POST["txtmobile"]
        obj.save()
        return redirect('profile')

     #select * from Registration where id=id
    return render(request,"designweb/dashboard/editprofile.html",{'res':obj})

def deleteprofile(request):
    id = request.GET["q"]
    obj = Registration.objects.get(pk=id)
    if request.method=="POST":
        obj.delete()
        return redirect('profile')
    return render(request,"designweb/dashboard/deleteprofile.html",{'res':obj})
def logout(request):
    del request.session['uname']
    return redirect('/designweb/login')    