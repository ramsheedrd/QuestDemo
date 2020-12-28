from django.shortcuts import render, HttpResponse, redirect
from .models import ProductModel
from .forms import ProductForm, ProductModelForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
# Create your views here.


class HomeView(ListView):
    template_name = 'index.html'
    queryset = ProductModel.objects.all().order_by('name') 
    context_object_name = 'products'


class GalleryView(TemplateView):
    template_name = 'gallery.html'


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = ProductModel
    context_object_name = 'product'


# class ProductAddView(FormView):
#     template_name = 'add-product.html'
#     form_class = ProductModelForm

#     def form_valid(self, form):
#         form.save()
#         return redirect('home')


class ProductAddView(CreateView):
    template_name = 'add-product.html'
    model = ProductModel
    fields = ['name', 'price', 'seller', 'category']
    success_url = '/'


class ProductUpdateView(UpdateView):
    template_name = 'edit-product.html'
    model = ProductModel
    fields = ['name', 'price', 'seller', 'category']
    success_url = '/'


class ProductDeleteView(DeleteView):
    template_name = 'delete-product.html'
    model = ProductModel
    success_url = '/'

