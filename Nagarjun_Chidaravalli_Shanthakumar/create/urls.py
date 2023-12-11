from django.urls import path
from create.views import createContact,add


urlpatterns = [
    path('', createContact, name="createContact"),
    path('add/', add, name="add"),
]
