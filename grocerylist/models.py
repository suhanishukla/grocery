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

class CityList(models.Model): 
    #"city","city_ascii","state_id","state_name","county_fips","county_name","lat","lng","population","density","source","military","incorporated","timezone","ranking","zips","id"
    city=models.CharField(max_length=255)
    #city_ascii=models.CharField(max_length=255)
    state_id=models.CharField(max_length=10)
    state_name=models.CharField(max_length=255)
    #county_fips=models.CharField(max_length=255)
    county_name=models.CharField(max_length=255)
    lat=models.FloatField()
    lng=models.FloatField()
    #population=models.IntegerField()
    #density=models.FloatField()
    #source=models.CharField(max_length=255)
    #military=models.BooleanField(default=False)
    #incorporated=models.BooleanField(default=False)
    #timezone=models.CharField(max_length=255)
    #ranking=models.IntegerField()
    zips=models.CharField(max_length=1000)
    #id=models.IntegerField()

class StoreList(models.Model): 
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    zip=models.CharField(max_length=255)





    
