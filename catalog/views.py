from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Product


def home(request):
    """Страница Home"""

    return render(request, "home.html")


def contact(request):
    """Страница Контакты"""

    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        print(message)
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html")


def product_info(request, product_id):
    """Страница с подробной инфо о товаре"""

    product = get_object_or_404(Product, id = product_id)
    context = {'product': product}

    return render(request, "product_info.html", context)


def product_list(request):
    """Страница вывод списка товаров"""

    products = Product.objects.all()
    context = {'products': products}

    return render(request, "product_list.html", context)
