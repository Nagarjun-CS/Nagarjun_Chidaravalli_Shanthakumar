
from django.urls import path
from confirm.views import confirm, deleteRecord

from home.views import homepage 

urlpatterns = [
    path('', confirm, name="confirm"),
    path('deleteRecord/', deleteRecord, name="deleteRecord")
   
]
