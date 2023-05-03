from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse
def twa(request):
    to=TopicForm()
    wo=WebpageForm()
    ao=AccessrecordForm()
    d={'to':to,'wo':wo,'ao':ao}
    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=AccessrecordForm(request.POST)
        if  tfd.is_valid() and wfd.is_valid() and afd.is_valid():
            STFD=tfd.save()
            NSWO=wfd.save(commit=False)
            NSWO.topic_name=STFD
            NSWO.save()
            NSAO=afd.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()
            return HttpResponse('Data submitted successfully')
        else:
            return HttpResponse('Data is invalid')


    return render(request,'twa.html',d)
