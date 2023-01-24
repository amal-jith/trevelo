from django. http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team

# Create your views here.

def demo(request):
    obj=Place.objects.all()
    tmem=Team.objects.all()
    return render(request,"index.html",{'result':obj, 'member':tmem})

#def operations(request):
#    x=int(request.GET['num1'])
 #   y=int(request.GET['num2'])
 #   add=x+y
 #   sub=x-y
 #   multi=x*y
  #  divid=x/y
  #  return render(request, 'result.html', {'add':add,'sub':sub,'mul':multi,'div':divid})



