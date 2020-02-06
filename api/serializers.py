from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()
    
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'quantity', 'subtotal', 'created_at']


        def create(self, validated_data):
            item_validated_data = validated_data.pop('item')
            item = Order.objects.create(**validated_data)
            item_serializer = self.fields['item']
            # for each in item_validated_data:
            #     each['item'] = item
            items = item_serializer.create(movie_validated_data)
            return item

    def get_subtotal(self, obj):
            return obj.price * obj.quantity