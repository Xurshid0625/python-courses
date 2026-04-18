from django.shortcuts import render
from main.models import Categories, Product


def index(request):
    
    category = Categories.objects.all()
    product = Product.objects.all()
    
    ctx = {
        'category': category,
        'product': product,
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