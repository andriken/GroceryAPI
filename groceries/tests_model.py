from django.test import TestCase
from groceries.models import GroceryItem


class GroceryItemTest(TestCase):
    """Test module for GroceryItem creqtion"""

    def setUp(self):
        GroceryItem.objects.create(
            title='Item 1',
            description='Item Description',
            price=10)

    def test_grocery_item(self):
        item = GroceryItem.objects.get(title='Item 1')
        self.assertEqual(item.price, 10)
