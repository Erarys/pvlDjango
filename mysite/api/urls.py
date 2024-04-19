from django.urls import path

from api.views import ProductApiView

app_name = 'api'


urlpatterns = [
    path('test/', ProductApiView.as_view(), name="test"),
]