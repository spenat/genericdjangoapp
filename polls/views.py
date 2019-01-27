from django.shortcuts import render
from django.http import HttpResponse
from .models import Thumb



# Create your views here.
def index(request):
    thumbs = Thumb.objects.all()
    context = {
        'thumbs': thumbs,
    }
    return render(request, 'polls/index.html', context)
    #return HttpResponse("Hello world")
    #return render("Hello world")


def health(request):
    return HttpResponse("I'm healthy yo")
