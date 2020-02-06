from rest_framework import viewsets, status
# from rest_framework.filters import OrderingFilter
from django_filters import rest_framework
from rest_framework.response import Response
from rest_framework import filters

from .models import Item

from .serializers import ItemSerializer

from django.db import models

from django.http import JsonResponse

class ItemViewSet(viewsets.ModelViewSet) :
    search_fields = ['name','price', 'created_at']
    filter_backends = (
        rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    filter_fields = ('name', 'price', 'created_at')
    serializer_class = ItemSerializer
    queryset = Item.objects.all()