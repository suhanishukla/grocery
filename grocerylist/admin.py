from django.contrib import admin
from .models import GroceryList
from .models import RecipeList

# Register your models here.
admin.site.register(GroceryList)
admin.site.register(RecipeList)
