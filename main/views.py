from django.shortcuts import render
from main.models import Categories




def index(request):
    
    category = Categories.objects.all()
    
    ctx = {
        'category': category
    }
    return render(request, 'main/index.html', ctx)
