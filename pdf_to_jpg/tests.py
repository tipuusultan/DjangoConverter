from django.test import TestCase
# from zipfile import ZipFile, ZIP_DEFLATED

# target = ['manage.py' , 'db.sqlite3']
# handle = ZipFile('demo.zip' , 'w')
# for t in target:
#     handle.write(t, compress_type=ZIP_DEFLATED)
# handle.close()


pdf_file_name = "FFuyck ferwf few"
if pdf_file_name.isspace():
    pdf_file_name.replace(" ", "_")
    print(pdf_file_name)