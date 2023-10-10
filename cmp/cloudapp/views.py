from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This will be the homepage where goes the Dashboard")

def resource(request):
    return render(request, 'resource.html')
    #return HttpResponse("This will be the Resource Management page")


def alert(request):
    return render(request, 'alert.html')
    #return HttpResponse("This will be the Monitoring & alerts page")

def management(request):
    return render(request, 'management.html')
    #return HttpResponse("This will be the Cost management page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This will be the About Us")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("This will be the contact us page")

def logout(request):
    return render(request, 'logout.html')
    #return HttpResponse("This will be the logout page")