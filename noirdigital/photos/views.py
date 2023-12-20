# photos/views.py
from django.shortcuts import render
from .models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photos/photo_list.html', {'photos': photos})
