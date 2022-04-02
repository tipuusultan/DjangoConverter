from django.shortcuts import render, redirect
from .models import PDF
from image_to_pdf.models import Tools
from django_pdf.settings import BASE_DIR
import os
from datetime import datetime
from zipfile import ZipFile , ZIP_DEFLATED
from random import randint
from django_pdf.settings import SITE_URL

# Create your views here.

def home(request):
    tools = Tools.objects.all()
    return render(request , 'index.html' , context={'tools':tools})




def pdf_to_image(request):
    ip_address = randint(1,32894839484875484343)
    downloadable_file = ''
    if request.method == 'POST':
        pdf_file = request.FILES['pdf']
        save_pdf = PDF(pdf=pdf_file)
        save_pdf.save()

        pdf_file_name = pdf_file.name
        if pdf_file_name.isspace():
            pdf_file_name.replace(" ", "_")
        file_dir = f'{BASE_DIR}\media\PDF\{pdf_file_name}'
        # rename the pdf
        
        # new_file_dir = f'{BASE_DIR}\media\PDF\{ip_address}.pdf'
        # os.rename(file_dir, new_file_dir)

        from pdf2image import convert_from_path
        images = convert_from_path(file_dir,500,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
        user_file_dir = f'{BASE_DIR}/media/{ip_address}'
        if not os.path.exists(user_file_dir):
            os.mkdir(user_file_dir)
        
        user_dir = f'media/{ip_address}'
        
        zip_files_name = []

        for i in range(len(images)):
            files_name = f'{user_dir}/page'+ str(i) +'.jpg'
            full_file_path = f'{user_dir}/{files_name}'
            images[i].save(files_name, 'JPEG')
            zip_files_name.append(files_name)
        
        zip_file_link = f'{user_dir}/Images.zip'
        handle = ZipFile(f'{user_dir}/Images.zip' , 'w')
        for z in zip_files_name:
            handle.write(z)

        context = {
            'download_link':zip_files_name,
            'zip_file_link':zip_file_link,
            'site_url':SITE_URL,
        }
        return render(request , 'pdf_to_image.html', context )
            
    return render(request , 'pdf_to_image.html')    

    