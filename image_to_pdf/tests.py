from django.test import TestCase

from PIL import Image
import img2pdf

pdf_path = 'C:/Users/Tipu Sultan/Desktop/python/Django/1/django_pdf/image_to_pdf/blank.pdf'
image1_path = 'C:/Users/Tipu Sultan/Desktop/python/Django/1/django_pdf/media/JPG_to_PDF/user_uploads/final_project_2qFKStx.png'

ready_a4_paper = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
layout_fun = img2pdf.get_layout_fun(ready_a4_paper)
with open(pdf_path,"wb") as f:
	f.write(img2pdf.convert(image1_path, layout_fun=layout_fun))

# from datetime import datetime

# date = datetime.now()
# print(date.minute)