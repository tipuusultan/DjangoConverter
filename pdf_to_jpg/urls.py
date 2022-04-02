from django.contrib import admin
from django.urls import path
from pdf_to_jpg import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('pdf-to-image/' , views.pdf_to_image , name='pdf_to_image'),
]
