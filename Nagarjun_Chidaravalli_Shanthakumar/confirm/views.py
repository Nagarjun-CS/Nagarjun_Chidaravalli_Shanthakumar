
from django.shortcuts import render
from datetime import datetime

from create.models import Create

# Create your views here.
def confirm(request):
    name = request.POST.get("name")
    return render(request, 'confirm.html',{'name':name})



def deleteRecord(request):
    deleteName = request.POST.get("name")
    print("---------------------------",deleteName)
    c = Create.objects.get(name=deleteName)
    print("**************************",c)
    c.delete()
    allData = Create.objects.all()
    return render(request, 'home.html', {'allData':allData})
