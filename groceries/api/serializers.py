from rest_framework import serializers
from ..models import GroceryItem


class GroceryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryItem
        fields = ['title', 'description', 'price', 'created']
