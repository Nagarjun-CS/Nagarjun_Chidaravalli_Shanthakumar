
from django.urls import path

from home.views import homepage
from update.views import saveUpdatedContact, updateContact 

urlpatterns = [
    path('', updateContact, name="updateContact"),
    path('saveUpdatedContact/', saveUpdatedContact, name="saveUpdatedContact")
]
