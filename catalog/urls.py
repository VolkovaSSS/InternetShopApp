from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactView

app_name = CatalogConfig.name

urlpatterns = [
    path("catalog/contact/", ContactView.as_view(), name="contact"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("", ProductListView.as_view(), name="product_list"),
]
