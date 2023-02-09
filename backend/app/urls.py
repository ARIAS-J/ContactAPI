from django.urls import path
from .views import Contactslist

urlpatterns = [
    path('contacts/', Contactslist)
]