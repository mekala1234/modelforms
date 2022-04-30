from django.http import HttpResponse
from django.shortcuts import render
from app.forms import *
# Create your views here.
def insert_topic(request):
    FO=TopicForm()
    d={'FO':FO}
    if request.method=='POST':
        FD=TopicForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('Inserted successfully')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    FO=WebpageForm()
    d={'FO':FO}
    if request.method=='POST':
        FD=WebpageForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('Webapage inserted')

    return render(request,'insert_webpage.html',d)