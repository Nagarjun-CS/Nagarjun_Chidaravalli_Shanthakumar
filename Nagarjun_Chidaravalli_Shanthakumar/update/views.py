from django.shortcuts import render

from create.models import Create

# Create your views here.
def updateContact(request):
    name = request.POST.get("name")
    '''contactDetails = Create.objects.filter(name=contact)
    name = ""
    for item in contactDetails:
        name = item.name'''
    return render(request, 'update.html',{'updateName':name})


def saveUpdatedContact(request):
    updateName = request.POST.get("updateName")
    print("name is -----------------",updateName)
    name = request.POST.get("name")
    email = request.POST.get("email")
    notes = request.POST.get("notes")

    contactDetails = Create.objects.get(name=updateName)

    contactDetails.name = name
    contactDetails.email = email
    contactDetails.notes = notes

    contactDetails.save()

    return render(request, 'update.html')