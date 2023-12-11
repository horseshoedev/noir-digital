from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def index(request):
    return render(request, "products/index.html", context)


def detail(product_id):
    return HttpResponse("you are looking at product %s." % product_id)
