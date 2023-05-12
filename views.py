from django.shortcuts import render

def index(request):
    return render(request,"carapp/index.html")
def about(request):
    return render(request,"carapp/about.html")
def services(request):
    return render(request,"carapp/service.html")
def booking(request):
    return render(request,"carapp/booking.html")
def contact(request):
    return render(request,"carapp/contact.html")
def dform(request):
    basiccourse= ["C","C++","DS","GO","HTML","JS","Mojo"]
    advancecourse=["Java","PYTHON"]
    cloudcourse=["AWS","DEVOPS","AZURE","SALESFORCE","GCM","BLOCKCHAIN"]
    coursefee = {"C":2500,"C++":3000,"DS":4500,"CORE Java":3500,"CORE Python":6500,"CORE .NET":10000,"CORE PHP":10000}
    if request.method=="POST":
        basic = request.POST['basic']
        advance= request.POST.getlist('advance')
        cloudcourse1 = request.POST['cloudcourse']
        coursefee1 = request.POST.getlist('completecourse')
        return render(request,"carapp/dform.html",{'basiccourse':basiccourse,'advancecourse':advancecourse,'cloudcourse':cloudcourse,'coursefee':coursefee,'resbasic':basic,'resadvance':advance,'rescloudcourse':cloudcourse1,'rescoursefee':coursefee1})     
    else:
      return render(request,"carapp/dform.html",{'basiccourse':basiccourse,'advancecourse':advancecourse,'cloudcourse':cloudcourse,'coursefee':coursefee})
