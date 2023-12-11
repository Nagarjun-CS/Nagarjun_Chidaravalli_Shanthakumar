from django.shortcuts import render

from create.models import Create

# Create your views here.
def showDetails(request):
    contact = request.POST.get("name")
    contactDetails = Create.objects.filter(name=contact)
    name = ""
    for item in contactDetails:
        name = item.name
    return render(request, 'details.html',{'details':contactDetails,'updateName':name})