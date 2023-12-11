
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
    #timestamp_str = "2023-12-03 05:09:48.153312"

    #timestamp_dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")

    c = Create.objects.get(name=deleteName)
    c.delete()
    allData = Create.objects.all()
    return render(request, 'home.html', {'allData':allData})
