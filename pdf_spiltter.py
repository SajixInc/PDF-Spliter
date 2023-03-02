import os
from PyPDF2 import PdfWriter, PdfReader 



def pdf_split(path,output_path=None):
    
    fname = os.path.splitext(os.path.basename(path))[0]
    
    pdf = PdfReader(path)
    leng=len(pdf.pages)
    for page in range(leng):
        pdf_writer = PdfWriter()
        # pdf_writer.addPage(pdf.getPage(page))
        pdf_writer.add_page(pdf.pages[page])
        # pdf_writer.pages[page]
        output_path=output_path
        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)
        op=(f"{output_path}\{output_filename}")
        with open(output_filename, 'wb') as out:
            
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))
    



def folder_pdf_spilter(folder_path):
    l = os.listdir(folder_path)
    le = len(l)
    for files in range(le):
        file = l[files]
        pdf_split(path=file)
        print(file)
        
# folder_pdf_spilter(folder_path='D:\projects\conversion\google\Google-Document-AI\Folder')
        
        

        
