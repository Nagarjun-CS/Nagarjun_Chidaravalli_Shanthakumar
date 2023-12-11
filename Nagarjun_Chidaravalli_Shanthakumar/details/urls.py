
from django.urls import path
from details.views import showDetails

from home.views import homepage 

urlpatterns = [
    path('', showDetails, name="showDetails"),
]
