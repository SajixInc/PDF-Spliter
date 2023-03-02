

<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/lifeeazy-logo1.png" align="right" width="250"/> <img src="https://drive.google.com/file/d/1XgGTluw7lWp-DROSa5Ri5S6E6wrQyHkh/view?usp=share_link" width="180"/> 

<h1 font-size="50px" align="center">PDF Split using Python</h1>


## About


PDF splitter is used for split  the hole pdf into pages using python, without coding simply call the function or method and mention the pdf path.I used other package  like PYPDF.
place the number of pdfs at one place and use the function (folder_pdf_spilter)  and mention the folder path then run the file there you got all pdfs into individual pdf pages.



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