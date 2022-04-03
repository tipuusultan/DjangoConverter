
from django.contrib import admin
from django.urls import path
from image_to_pdf import views

urlpatterns = [
    path('' , views.home , name='home'),
]
