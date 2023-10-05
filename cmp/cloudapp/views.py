from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This will be the homepage where goes the Dashboard")

def resource(request):
    return HttpResponse("This will be the Resource Management page")


def alert(request):
    return HttpResponse("This will be the Monitoring & alerts page")

def management(request):
    return HttpResponse("This will be the Cost management page")

def about(request):
    return HttpResponse("This will be the About Us")

def contact(request):
    return HttpResponse("This will be the contact us page")
