from django.test import TestCase
from zipfile import ZipFile, ZIP_DEFLATED

from pdf2image import convert_from_path
pages = convert_from_path(r'C:\Users\Tipu\Downloads\3PL.pdf', 500, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')

#Saving pages in jpeg format

for page in pages:
    page.save('out.jpg', 'JPEG')