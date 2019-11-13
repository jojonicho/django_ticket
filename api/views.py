from rest_framework import viewsets, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .models import Movie, Seat, Order

from .serializers import MovieSerializer, SeatSerializer, OrderSerializer

from django.db import models

from django.http import JsonResponse

from .utils import generate_id, generate_time


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def create_movie(self, request):
        if request.method == 'PUT':
            name = int(request.POST['film_id'])
            desc = int(request.POST['film_id'])
            play_date_time = int(request.POST['kursi_id'])
            created_at = generate_id()
            movie = Movie(name=name, desc=desc,
                          play_date_time=play_date_time, created_at=created_at)
            Movie.objects.create(movie)
            serializers = MovieSerializer(movie, many=True)
            return JsonResponse(serializers.data)
        else:
            return JsonResponse(data=None, status=405)


class SeatViewSet(viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()

    def create_seat(self, request):
        if request.method == 'PUT':
            film_id = int(request.POST['film_id'])
            kursi_id = int(request.POST['kursi_id'])
            ticket_id = generate_id()
            seat = Seat(film_id=film_id, kursi_id=kursi_id,
                        ticket_id=ticket_id)
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
