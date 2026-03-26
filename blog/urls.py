from django.urls import path
from blog.apps import BlogConfig
# from blog.views import ProductListView, ProductDetailView, ContactView

app_name = BlogConfig.name

# urlpatterns = [
#     path("catalog/contact/", ContactView.as_view(), name="contact"),
#     path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
#     path("", ProductListView.as_view(), name="product_list"),
#     ]
