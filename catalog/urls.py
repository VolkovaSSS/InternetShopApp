from django.urls import path
from catalog.apps import CatalogConfig
from catalog import views

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("product_info/<int:product_id>", views.product_info, name="product_info"),
    path("product_list/", views.product_list, name="product_list"),
]
