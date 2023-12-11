from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from create.models import Create



def createContact(request):
    return render(request,'create.html')

def add(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    notes = request.POST.get("notes")

    contactDetails = Create.objects.filter(name=name)

    if contactDetails:
        print(contactDetails)
        return render(request, 'create.html',{'error':'contact found'})
    else:
        print(contactDetails)
        print("nno record--------------------")

        contact = Create()
        contact.name = name
        contact.email = email
        contact.notes = notes
        
        current_datetime_utc = timezone.now()
        contact.time = current_datetime_utc

        print("hi there",current_datetime_utc)


        contact.save()

        contactList = Create.objects.all()

        return render(request, 'home.html',{'contactList':contactList})