from ..models import GroceryItem
from .serializers import GroceryItemSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GetGroceryItemListTest(APITestCase):
    """ Test module for GET all grocery item ist API """
    def setUp(self):
        # create temporarily items for test
        GroceryItem.objects.create(
            title='Item 1',
            description='Item Description',
            price=10)
        GroceryItem.objects.create(
            title='Item 2',
            description='Item 2 Description',
            price=20)

    def test_grocery_item_list(self):
        # get api response
        url = reverse('groceries:grocery_list')
        response = self.client.get(url)
        # get data from database
        items = GroceryItem.objects.all()
        serializer = GroceryItemSerializer(items, many=True)
        self.assertEqual(dict(response.data)['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
