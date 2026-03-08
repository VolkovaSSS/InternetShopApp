from django.shortcuts import render
from django.http import HttpResponse


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


def base(request):
    """Страница Home"""

    return render(request, "base.html")
