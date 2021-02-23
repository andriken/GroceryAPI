from rest_framework import generics, filters
from ..models import GroceryItem
from .serializers import GroceryItemSerializer


class GroceryItemListView(generics.ListAPIView):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created', 'price']

