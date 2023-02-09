import json
from django.http import JsonResponse
from drf_yasg import openapi
from rest_framework.decorators import api_view
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from .serializers import ContactSerializer
from .models import Contacts



@swagger_auto_schema(method=['GET'])
@api_view(['GET'])
def Contactslist(request):
    if request.method == 'GET':
        # Queryset
        contacts = Contacts.objects.all()
        # Serializer
        serializer = ContactSerializer(contacts, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)