from django.contrib import admin
from .models import GroceryList
from .models import RecipeList
#from .models import ShoppingCart

# Register your models here.
admin.site.register(GroceryList)
admin.site.register(RecipeList)
#admin.site.register(ShoppingCart)
