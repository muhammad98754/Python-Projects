"""First, we need to import all the packages. You need pdf2image to convert PDF files to ppm image files.

We also need to manipulate the paths to join and rename text files, so we import the os and sys packages. The following part calls a PIL library and imports the image with pytesseract:"""

import pdf2image
import os, sys
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#Now we need to initialize the path of your documents and the counter to be used later in the pdf extract function to count your documents in the folder:
PATH = 'Enter your path'

#initialize the counter that you will use later in your pdf extraction function
i = 1

#Now, we need to delete some unrequired files from our pdf files, for this I will create a new function:

def delete_ppms():
  for file in os.listdir(PATH):
    if '.ppm' in file or '.DS_Store' in file:
      try:
          os.remove(PATH + file)
      except FileNotFoundError:
          pass
        
# Now we need to sort the pdf files according to their types. I will start this by creating to lists one for pdf files and one for Docx files because these two types are the most used pdf file types:

pdf_files = []
docx_files = []

# append document names into the lists by their extension type
for f in os.listdir(PATH):
  full_name = os.path.join(PATH, f) 
  if os.path.isfile(full_name):
    name = os.path.basename(f)
    filename, ext = os.path.splitext(name)
    if ext == '.pdf':
      pdf_files.append(name)
    elif ext == ('.docx'):
      docx_files.append(name)
#Now we can finally extract text from PDF files. Here is the pdf_extract function. First, it prints the name of each file from which the text is extracted. Depending on the size of the document, extracting text may take some time.

#This print function will help you see which file is currently checked out:

def pdf_extract(file, i):
  print("extracting from file:", file)
  delete_ppms()
  images = pdf2image.convert_from_path(PATH + file, output_folder=PATH)
  j = 0
  for file in sorted (os.listdir(PATH)):
      if '.ppm' in file and 'image' not in file:
        os.rename(PATH + file, PATH + 'image' + str(i) + '-' + str(j) + '.ppm')
        j += 1
  j = 0
  f = open(PATH +'result{}.txt'.format(i), 'w')
  files = [f for f in os.listdir(PATH) if '.ppm' in f]

  for file in sorted(files, key=lambda x: int(x[x.index('-') + 1: x.index('.')])):
      temp = pytesseract.image_to_string(Image.open(PATH + file))
      f.write(temp)
  f.close()
  
 #Now, we can use our function to extract from all the PDF files using Python:

for i in range(len(pdf_files)):
  pdf_file = pdf_files[i]
  pdf_extract(pdf_file, i)

  
#Now after running the function if you will go to the directory you will see a text file by the name of result1.txt with all the text extracted from the PDF file.
