from django.shortcuts import render
from blog_app.models import blogpost

import requests

from django import forms




def homepage(request):
    articoli_database = blogpost.objects.all()
    articoli_database = articoli_database.order_by('-data')[:4]
    context = {'articoli': articoli_database}
    return render(request, 'home.html', context)

def about_us_page(request):
    articoli_database = blogpost.objects.all()
    articoli_database = articoli_database.order_by('-data')[:4]
    context = {'articoli': articoli_database}
    return render(request, 'about_us.html', context)


