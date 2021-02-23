from django.urls import path
from . import views

app_name = 'groceries'

urlpatterns = [
    path('items/', views.GroceryItemListView.as_view(), name='grocery_list'),
]
