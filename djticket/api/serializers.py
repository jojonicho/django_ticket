from rest_framework import serializers
from .models import Movie, Seat, Order


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'desc', 'play_date_time']
    # def create(self, validated_data):
    #     # seat = Seat.objects.get(
    #     #     pk=validated_data.pop('assignment_set').get('id'))
    #     movie_validated_data = validated_data.pop('movie')
    #     seat = Seat.objects.create(**validated_data)
    #     movie_serializer = self.fields['movie']
    #     for each in movie_validated_data:
    #         each['seat'] = seat
    #     movies = movie_serializer.create(movie_validated_data)
    #     # .objects.create(Order=order, Equipment=Equipment)
    #     return seat


class SeatSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)
    # movie = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Seat
        fields = ['id', 'seat_num', 'movie']

    def create(self, validated_data):
        # seat = Seat.objects.get(
        #     pk=validated_data.pop('assignment_set').get('id'))
        movie_validated_data = validated_data.pop('movie')
        seat = Seat.objects.create(**validated_data)
        movie_serializer = self.fields['movie']
        for each in movie_validated_data:
            each['seat'] = seat
        movies = movie_serializer.create(movie_validated_data)
        # .objects.create(Order=order, Equipment=Equipment)
        return seat
    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned queries by filtering against
    #     a `sport` and `name` query parameter in the URL.
    #     """
    #     queryset = Seat.objects.all()
    #     movie = self.request.query_params.get('movie', None)
    #     # name = self.request.query_params.get('name', None)
    #     if movie is not None:
    #         movie = movie.title()
    #         queryset = queryset.filter(movie=movie)
    #     # if name is not None:
    #     #     queryset = queryset.filter(name=name)
    #     return queryset

    # def to_representation(self, instance):
    #     representation = super(EquipmentSerializer,
    #                            self).to_representation(instance)
    #     representation['assigment'] = AssignmentSerializer(
    #         instance.assigment_set.all(), many=True).data
    #     return representation


class OrderSerializer(serializers.ModelSerializer):
    seat = SeatSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'seat']

    def create(self, validated_data):
        seat_validated_data = validated_data.pop('seat')
        order = Order.objects.create(**validated_data)
        seat_serializer = self.fields['seat']
        for each in seat_validated_data:
            each['order'] = order
        seats = seat_serializer.create(seat_validated_data)
        # .objects.create(Order=order, Equipment=Equipment)
        return order

    # def to_representation(self, instance):
    #     representation = super(EquipmentSerializer,
    #                            self).to_representation(instance)
    #     representation['assigment'] = AssignmentSerializer(
    #         instance.assigment_set.all(), many=True).data
    #     return representation
