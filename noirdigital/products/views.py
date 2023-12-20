# from django.http import HttpResponse
from django.shortcuts import render
# from django.template import context
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render (request, 'products/product_list.html', {'products': products})


# def index(request):
#     return render(request, "products/index.html", context)


# def detail(product_id):
#     return HttpResponse("you are looking at product %s." % product_id)
