from django.db import models
import uuid
# Create your models here.
class GroceryList(models.Model): 
    type=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    rating=models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    inlist=models.BooleanField(default=True)

class RecipeList(models.Model): 
    name=models.CharField(max_length=255)
    servingsize=models.CharField(max_length=10)
    ingredients_list = models.CharField(max_length=255)
    directions = models.CharField(max_length=1000)



    
