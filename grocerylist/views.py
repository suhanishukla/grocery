from django.http import HttpResponse
from django.template import loader 
from .models import GroceryList
from .models import RecipeList
import csv 
from django.shortcuts import render 
from django.db.models import Q
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status 
from .serializer import * 
def readcsvfile(): 
    with open('output.csv','r') as file: 
        csvreader = csv.reader(file)
        for row in csvreader: 
            GroceryList.objects.create(type=row[0], name=row[1], price=row[2],rating=row[3],inlist=False)
            
"""def grocerylist(request): 
    GroceryList.objects.all().delete()
    with open('groceryimagesupdated.csv','r') as file: 
        csvreader = csv.reader(file)
        for row in csvreader: 
            GroceryList.objects.create(type=row[0], name=row[1], price=row[3],description=row[2],inlist=False, imagelink=row[5], quantity=row[4])
            
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = (Q(type__icontains=q) | Q(name__icontains=q))
        filteredlist = GroceryList.objects.filter(multiple_q)
        mygrocerylist = []

        for item in filteredlist: 
            if item not in mygrocerylist: 
                print(item.id)
                mygrocerylist.append(item)
        print("there are "+str(len(mygrocerylist))+" in mygrocerylist")
    else: 
        mygrocerylist = GroceryList.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mygrocerylist': mygrocerylist,
    }
    
    return HttpResponse(template.render(context, request))"""
def grocerylist(request): 
    # Read CSV file and create GroceryList objects
    GroceryList.objects.all().delete()
    with open('groceryimagesupdated.csv','r') as file: 
        csvreader = csv.reader(file)
        for row in csvreader: 
            GroceryList.objects.create(type=row[0], name=row[1], price=row[3],description=row[2],inlist=False, imagelink=row[5], quantity=row[4])
            
    # Get search query from request
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(type__icontains=q) | Q(name__icontains=q))
        mygrocerylist = GroceryList.objects.filter(multiple_q)
    else: 
        mygrocerylist = GroceryList.objects.all()

    # Pagination
    default_page = 1
    page = request.GET.get('page', default_page)
    items_per_page = 8
    paginator = Paginator(mygrocerylist, items_per_page)

    try:
        mygrocerylist_page = paginator.page(page)
    except PageNotAnInteger:
        mygrocerylist_page = paginator.page(default_page)
    except EmptyPage:
        mygrocerylist_page = paginator.page(paginator.num_pages)

    # Render template with context
    template = loader.get_template('index.html')
    context = {
        'mygrocerylist': mygrocerylist_page,
    }
    
    return HttpResponse(template.render(context, request))


def recipelist(request): 
    
    if 'q' in request.GET:
        q = request.GET['q']
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

def homePage(request): 
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(name__icontains=q) | Q(city__icontains=q))
        mystorelist = StoreList.objects.filter(multiple_q)
    else: 
        mystorelist = StoreList.objects.all().values()
    template = loader.get_template('home.html')
    
    context = {
        'mystorelist': mystorelist,
    }
    return HttpResponse(template.render(context, request))