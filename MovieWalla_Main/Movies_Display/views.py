from django.shortcuts import render
import csv
from django.http import HttpResponse
# Create your views here.
import datetime
def home(request):
    d=datetime.datetime.now()
    mv={}
    mv['dt']=d
    return render(request,'index.html',mv)
def store(request):
    return render(request,'store.html')

def cus(request):
    name=request.GET['name']
    email=request.GET['email']
    message=request.GET['message']
    with open('cus.txt','a') as f:
        gg=name+','+email+','+message+'\n'
        f.write(gg)
        f.close()
    return HttpResponse('I have Received your message i will get back to you soon')