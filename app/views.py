from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
def insert_topics(request):
    tn = input('enter topic name :')
    TO = topics.objects.get_or_create(topic_name = tn)
    if TO[1]:
       
        d = {'topics':topics.objects.all()}
        return render(request,'display_topics.html',d)
        #return HttpResponse('topic is created ')
    else:
        return HttpResponse('topic is not created ')
    


