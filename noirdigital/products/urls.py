from django.urls import path
from .views import product_list

app_name = 'products'
urlpatterns = [
    path("", product_list, name="product_list"),
    # ex: product/example
    # path("<int:product_id>/", views.detail, name="detail")
]
