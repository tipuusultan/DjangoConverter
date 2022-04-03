from django.contrib import admin
from image_to_pdf.models import JPG_to_PDF, Tools

# Register your models here.
admin.site.register(Tools)
admin.site.register(JPG_to_PDF)
