from django.shortcuts import render
from random import randint
from image_to_pdf.models import JPG_to_PDF
from django_pdf.settings import BASE_DIR , SITE_URL
import os

# Create your views here.

def home(request):
    ip_address = randint(1,32894839484875484343)
    downloadable_file = ''
    if request.method == 'POST':
        jpg_file = request.FILES['jpg']
        save_jpg = JPG_to_PDF(images = jpg_file)
        save_jpg.save()

        import img2pdf

        punctuations = [',' , '<' , '>' , '/' , '?' , ':' , ';' , '}' , ']' , '[' , '{' , '(' , ')']

        

        image_name = jpg_file.name
        image_path = f'media/JPG_to_PDF/user_uploads/{image_name}'
        pdf_path = f'{BASE_DIR}/media/JPG_to_PDF/user_pdfs/{image_name}.pdf'
        print(image_path)
        
        ready_a4_paper = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
        layout_fun = img2pdf.get_layout_fun(ready_a4_paper)
        with open(pdf_path,"wb") as f:
        	f.write(img2pdf.convert(image_path, layout_fun=layout_fun)) 

        final_pdf =  f'{SITE_URL}media/JPG_to_PDF/user_pdfs/{image_name}.pdf'
        context = {
            'pdf_path': final_pdf,
            
        }
        return render(request , 'jpg_to_pdf.html' , context)

    return render(request , 'jpg_to_pdf.html')
