from django.urls import path

from .views import (
    HomeView,
    ShopView,
    partners,
    project,
    about,
    menu,
    reviews,
)

app_name = "coffee_shop"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('partners/', partners, name='partners'),
    path('project/', project, name='project'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('reviews/', reviews, name='reviews')
]
