from django.urls import path
from .views import HomeView, CreateProductView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add', CreateProductView.as_view(), name='add-product')

]
