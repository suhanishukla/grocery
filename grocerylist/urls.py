from django.urls import path 
from . import views 

urlpatterns = [
    path('grocerylist/', views.grocerylist, name='grocerylist'), 
    path('recipes/', views.recipelist, name='recipelist'),
    path('cart/', views.shoppingCart, name='shoppingCart'),
]