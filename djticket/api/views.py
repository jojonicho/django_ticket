from rest_framework import viewsets

from .models import Movie, Seat, Order

from .serializers import MovieSerializer, SeatSerializer, OrderSerializer

from django.db import models

from django.http import JsonResponse

from .utils import generate_id, generate_time


# class MatchViewSet(viewsets.ModelViewSet):
#     """
#     retrieve:
#     Return the given match.
#     list:
#     Return a list of all the existing matches.
#     create:
#     Create a new match instance.
#     """
#     queryset = Match.objects.all()
#     serializer_class = MatchListSerializer  # for list view
#     detail_serializer_class = MatchDetailSerializer  # for detail view
#     filter_backends = (DjangoFilterBackend, OrderingFilter,)
#     ordering_fields = '__all__'

#     def get_serializer_class(self):
#         """
#         Determins which serializer to user `list` or `detail`
#         """
#         if self.action == 'retrieve':
#             if hasattr(self, 'detail_serializer_class'):
#                 return self.detail_serializer_class
#         return super().get_serializer_class()

#     def get_queryset(self):
#         """
#         Optionally restricts the returned queries by filtering against
#         a `sport` and `name` query parameter in the URL.
#         """
#         queryset = Match.objects.all()
#         sport = self.request.query_params.get('sport', None)
#         name = self.request.query_params.get('name', None)
#         if sport is not None:
#             sport = sport.title()
#             queryset = queryset.filter(sport__name=sport)
#         if name is not None:
#             queryset = queryset.filter(name=name)
#         return queryset

#     def create(self, request):
#         """
#         to parse the incoming request and create a new match or update
#         existing odds.
#         """
#         message = request.data.pop('message_type')
#         # check if incoming api request is for new event creation
#         if message == "NewEvent":
#             event = request.data.pop('event')
#             sport = event.pop('sport')
#             # for now we have only one market
#             markets = event.pop('markets')[0]
#             selections = markets.pop('selections')
#             sport = Sport.objects.create(**sport)
#             markets = Market.objects.create(**markets, sport=sport)
#             for selection in selections:
#                 markets.selections.create(**selection)
#             match = Match.objects.create(**event, sport=sport, market=markets)
#             return Response(status=status.HTTP_201_CREATED)
#         # check if incoming api request is for updation of odds
#         elif message == "UpdateOdds":
#             event = request.data.pop('event')
#             markets = event.pop('markets')[0]
#             selections = markets.pop('selections')
#             for selection in selections:
#                 s = Selection.objects.get(id=selection['id'])
#                 s.odds = selection['odds']
#                 s.save()
#             match = Match.objects.get(id=event['id'])
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    # filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    # ordering_fields = '__all__'

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
