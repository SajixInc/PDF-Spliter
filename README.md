

<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/lifeeazy-logo1.png" align="right" width="250"/> <img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/pdf_split_image-removebg-preview.png" width="180"/> 

<h1 font-size="50px" align="center">PDF Split using Python</h1>


## About


PDF splitter is used for split  the whole pdf into multiple pages using python, for this we can call this simple function or method for which I used package called PYPDF.

We have to Place the number of pdfs at one place and use the function (folder_pdf_spilter)  and mention the folder path then run the file there you got all pdfs into individual pdf pages.

This function takes in two arguments: file_path is the path to the PDF file that needs to be split, and pages is a list of tuples representing the page ranges to be extracted. Each tuple consists of two integers: the starting page number and the ending page number. For example, if pages is [(1, 3), (5, 6)], the function will create two output PDF files: "output_1-3.pdf" containing pages 1 to 3, and "output_5-6.pdf" containing pages 5 to 6.


## Features

- Split the pdf
- integrate to Tkinter,
- Django restframe work etc.
- free of cost 
- easy to use


## Development Environment (Local)
#### System Requirements
💻 Supported Os:
* Ubuntu (18.04/20.04)
* Windows
* Mac Os
* CentOS (7/8)
* Red Hat Enterprise Linux

⚙️Hardware Requirements:



💡 Before you begin, make sure you have the  installed [**Python**](python.org)

# Usage
* clone the respositry.

### installion packages
To install Required packages run this command:
```bash
  pip install -r requirements.txt 
```

Before that, you have to ensure the your path location, where the pdf_splitter.py is


Now import the file wherever we want to call 

```bash
import pdf_spiltter
```
<h1 font-size="20px" >or</h1>

```bash
from pdf_spiltter import *
```
sample code:
```bash
pdf_path =' give the pdf path'
pdf_split(pdf_path)

```

if you want to split the bunch of file 
```bash
folder_pdf_path =' give the pdf path'
folder_pdf_spilter(folder_pdf_path)

```

To run the python  file  
run this command

```bash
python --file path 
```
