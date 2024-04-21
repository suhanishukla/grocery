from django.urls import path 
from django.contrib import admin 
#from django.conf.urls import url 
#from app.views import *
from . import views 

urlpatterns = [
    #path('reactview/', ReactView.as_view(), name="anything")
    path('grocerylist/', views.grocerylist, name='grocerylist'), 
    path('recipes/', views.recipelist, name='recipelist'),
    path('cart/', views.shoppingCart, name='shoppingCart'),
    path('home/', views.homePage, name='home'),
]