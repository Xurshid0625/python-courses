from django.shortcuts import render
from main.models import Categories, Product, New


def index(request):
    
    category = Categories.objects.all()
    product = Product.objects.all().order_by('-id')[:3]
    new  = New.objects.all().order_by('-id')[:1]
    
    ctx = {
        'category': category,
        'product': product,
        'new':new,
    }
    return render(request, 'main/index.html', ctx)


def shop(request):
    
    product = Product.objects.all()
    
    ctx = {
        'product': product,
    }
    
    return render(request,'main/product.html',ctx)

def product(request, id):
    
    product_info = Product.objects.filter(categories_id=id)
    
    ctx = {
        'product_info': product_info,
    }
    
    return render(request, 'main/product_info.html',ctx)


def product_info(request, id):
    
    product_info = Product.objects.get(id=id)
    
    ctx = {
        'product_info': product_info,
    }
    
    return render(request, 'main/product_inform.html', ctx)

def new(request):
    
    new = New.objects.all()
    
    ctx = {
        'new':new,
    }
    
    return render(request, 'main/new.html',ctx)
