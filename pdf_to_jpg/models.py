from django.db import models

# Create your models here.
class PDF(models.Model):
    pdf = models.FileField(upload_to='PDF', max_length=100)

    def __str__(self):
        return self.pdf.name
    