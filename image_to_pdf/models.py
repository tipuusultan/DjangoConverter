from django.db import models
from datetime import datetime

from django.db.models.base import Model

# Create your models here.
class JPG_to_PDF(models.Model):
    images = models.ImageField(upload_to='JPG_to_PDF/user_uploads')
    time = models.TimeField(default=datetime.now())

    def __str__(self): 
        return self.images.name
    
class Tools(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    