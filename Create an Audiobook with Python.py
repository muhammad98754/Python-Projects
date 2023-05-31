"""PyPDF2 allows manipulation of pdf in memory. This python library is capable of tasks such as:

extract information about the document, such as title, author, etc.
document division by page
merge documents per page
cropping pages
merge multiple pages into one page
encrypt and decrypt PDF files
and more.
I will use this library to split the pdf file page by page, then read the text on each page, then send the text to the next step in the process to create an audiobook with Python."""

import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('file.pdf', 'rb'))

"The pyttsx3 library is capable of converting text to speech offline. The text that we read from a pdf is then fed as an input to the text-to-speech engine:

import pyttsx3
speaker = pyttsx3.init()

"Now the next step in the process is to loop the process for each page of the pdf file and stop the pyttsx3 speaker engine last:

for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

"Now the next step is to save the audio as mp3 file:

engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()
