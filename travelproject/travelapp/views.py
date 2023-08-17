from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import members

# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=members.objects.all()

    return render(request,'index.html',{'result':obj,'result1':obj1})

#def addition(request):
 #  y=int(request.GET['num2'])
 #   result=x+y

 #   return render(request,'result.html',{'result':result})

