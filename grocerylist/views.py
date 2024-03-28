from django.http import HttpResponse
from django.template import loader 
from .models import GroceryList
from .models import RecipeList
import csv 
from django.shortcuts import render 
from django.db.models import Q

def grocerylist(request): 
    with open('output.csv','r') as file: 
        csvreader = csv.reader(file)
        for row in csvreader: 
            GroceryList.objects.create(type=row[0], name=row[1], price=row[2],rating=row[3],inlist=False)
    if 'q' in request.GET:
        q = request.GET['q']
        #mygrocerylist = GroceryList.objects.filter(type__icontains=q)
        multiple_q = Q(Q(type__icontains=q) | Q(name__icontains=q))
        mygrocerylist = GroceryList.objects.filter(multiple_q)
    else: 
        mygrocerylist = GroceryList.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mygrocerylist': mygrocerylist,
    }
    
    return HttpResponse(template.render(context, request))
def recipelist(request): 
    with open('recipes.csv','r') as file: 
        csvreader = csv.reader(file)
        for row in csvreader: 
            RecipeList.objects.create(name=row[0], servingsize=row[1], ingredients_list=row[2],directions=row[3])
    if 'q' in request.GET:
        q = request.GET['q']
        #mygrocerylist = GroceryList.objects.filter(type__icontains=q)
        multiple_q = Q(Q(name__icontains=q) | Q(ingredients_list__icontains=q))
        myrecipelist = RecipeList.objects.filter(multiple_q)
    else: 
        myrecipelist = RecipeList.objects.all().values()
    template = loader.get_template('recipedisplay.html')
    context = {
        'myrecipelist': myrecipelist,
    }
    return HttpResponse(template.render(context, request))


def shoppingCart(request): 
    template = loader.get_template('cart.html')
    hide_specific_part = '/cart' in request.path
    context = {
       'hide_specific_part': hide_specific_part,
    }
    
    return HttpResponse(template.render(context,request))

