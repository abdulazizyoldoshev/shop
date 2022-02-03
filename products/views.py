from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import ProductModel
from .form import ProductModelForm


class HomeView(TemplateView):
    template_name = 'base.html'


class CreateProductView(CreateView):
    template_name = 'main/add-product.html'
    model = ProductModel
    success_url = "/"
    form_class = ProductModelForm
