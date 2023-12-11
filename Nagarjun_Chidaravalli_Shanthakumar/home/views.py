from django.http import HttpResponse
from django.shortcuts import render

from create.models import Create

# Create your views here.
def homepage(request):
    allData = Create.objects.all()
    return render(request, 'home.html',{'allData':allData})
