from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def display_topics(request):
    QST=Topic.objects.all()
    d={'topic':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)

def AccessRecords(request):
    ASR=AccessRecords.objects.all()
    d={'AccessRecord':ASR}
    return render(request,'AccessRecords.html',d)
    