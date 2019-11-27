from rest_framework import viewsets, status
# from rest_framework.filters import OrderingFilter
from django_filters import rest_framework
from rest_framework.response import Response
from rest_framework import filters

from .models import Movie, Seat, Order

from .serializers import MovieSerializer, SeatSerializer, OrderSerializer

from django.db import models

from django.http import JsonResponse

from .utils import generate_id, generate_time


class MovieViewSet(viewsets.ModelViewSet):
    search_fields = ['name', 'desc']
    # filter_backends = (filters.SearchFilter,)
    filter_backends = (
        rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    filter_fields = ('name', 'desc')
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def create_movie(self, request):
        if request.method == 'POST':
            name = request.POST['name']
            desc = request.POST['desc']
            play_date_time = request.POST['play_date_time']
            mov_id = generate_id()
            movie = Movie(name=name, desc=desc,
                          play_date_time=play_date_time)
            Movie.objects.create(movie)
            serializers = MovieSerializer(movie, many=True)
            return JsonResponse(serializers.data)
        else:
            return JsonResponse(data=None, status=405)


class SeatViewSet(viewsets.ModelViewSet):
    search_fields = ['seat_num']
    filter_backends = (filters.SearchFilter,)
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()

    def create_seat(self, request):
        if request.method == 'POST':
            seat_num = request.POST['seat_num']
            movie = request.POST['movie']
            ticket_id = generate_id()
            seat = Seat(seat_num=seat_num, movie=movie)
            # ticket_id=ticket_id)
            Seat.objects.create(seat)
            serializers = SeatSerializer(seat, many=True)
            return JsonResponse(serializers.data)
        else:
            return JsonResponse(data=None, status=405)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # filter_backends = (OrderingFilter)
    # ordering_fields = '__all__'
