from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from coffee_shop.forms import OrderCreateForm
from coffee_shop.models import Product, Order


class HomeView(View):

    def get(self, request: HttpRequest):
        return render(request, "coffee_shop/home.html")


class ShopView(View):

    def get(self, request: HttpRequest):
        user = request.user
        context = {
            "goods": Product.objects.all(),
            "form": OrderCreateForm(user=user),
            "orders": Order.objects.filter(user=user)
        }
        return render(request, "coffee_shop/shop.html", context)

    def post(self, request: HttpRequest):
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
        return render(request, "coffee_shop/shop.html", {"form": form})


"""Мусор"""


def partners(request):
    return render(request, "coffee_shop/partners.html")


def project(request):
    return render(request, "coffee_shop/project.html")


def about(request):
    return render(request, "coffee_shop/about.html")


def menu(request):
    context = {
        "form": OrderCreateForm()
    }
    return render(request, "coffee_shop/menu.html", context)


def reviews(request):
    return render(request, "coffee_shop/reviews.html")
