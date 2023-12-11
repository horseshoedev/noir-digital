from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path("products/", views.index, name="index"),
    # ex: product/example
    path("<int:product_id>/", views.detail, name="detail")
]
