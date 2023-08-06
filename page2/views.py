from django.shortcuts import render
from .models import PersonalInfo

def info(request):
    all= PersonalInfo.objects.all()
    return render(request,'two.html',{'info':all})

def hello(request):
    person={'name':'ali'}
    return render(request,'hello.html', context= person)

def detail(request,personalinfo_id):
    personalinfo=PersonalInfo.objects.get(id=personalinfo_id)
    return render(request,'detail.html',{'personalinfo': personalinfo})
   
