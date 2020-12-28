"""quest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('gallery/', views.GalleryView.as_view(), name= "gallery"),
    path('product/add/', views.ProductAddView.as_view(), name= "add_product"),
    path('product/edit/<pk>/', views.ProductUpdateView.as_view(), name= "edit_product"),
    path('product/delete/<pk>/', views.ProductDeleteView.as_view(), name= "del_product"),
    path('product/detail/<pk>/', views.ProductDetailView.as_view(), name= "detail_product"),



]
