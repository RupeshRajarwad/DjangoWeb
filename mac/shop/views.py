from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
    #products=Product.objects.all()
    #print(products)
    #n=len(products)
    #nslides=n//4+ceil((n/4)-(n//4))
    allProds = []
    catprods = Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n=len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,nslides),nslides])

    #params={'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    #allProds = [[products,range(1,nslides),nslides],
    #          [products,range(1,nslides),nslides]]
    params = {'allProds':allProds}


    return render(request,'index.html',params)

def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')

def tracker(request):
    return render(request, 'tracker.html')

def search(request):
    return render(request,'search.html')

def prodView(request):
    return render(request,'prodview.html')

def checkout(request):
    return render(request,'checkout.html')


