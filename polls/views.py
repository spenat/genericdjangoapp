from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def index(request):
    return HttpResponse("Hello world")
    #return render("Hello world")


def health(request):
    return HttpResponse("I'm healthy yo")
