from django.shortcuts import render, redirect
from .models import quotes,author,category,movie
from datetime import date

# Create your views here.
def home(request):
    categories=category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def get_by_category(request,id):    
    q = quotes.objects.filter(category=id)
    c=category.objects.filter(id=id)
    return render(request,'quotes.html', {'category':c,'quote':q})

def get_by_author(request,id):
    q = quotes.objects.filter(author=id)
    a=author.objects.filter(id=id)
    return render(request,'quotes.html', {'author':a ,'quote':q})

def get_by_movie(request,id):
    q = quotes.objects.filter(movie=id)
    m=movie.objects.filter(id=id)
    return render(request,'quotes.html', {'movie':m ,'quote':q})

def get_by_birthday(request):
    m = date.today().month
    d = date.today().day
    q = quotes.objects.filter(author__birthdate__month =m ,author__birthdate__day =d)    
    return render(request,'quotes.html', {'quote':q})

def author_list(request):
    a = author.object.all()
    return render(request,'author_list.html', {'author':a})

