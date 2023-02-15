from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    
    
class PersonDetail(generics.RetrieveDestroyAPIView):
        queryset = Person.objects.all()
        serializer_class = PersonSerializer
        
        
        
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_root(request, format=None):
    return Response({
        'persons': reverse('person', request=request, format=format)
    })
        
