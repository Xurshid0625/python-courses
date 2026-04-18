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
