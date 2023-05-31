#I will simply start with importing all the necessary libraries that we need for this task to create a program that takes the text of an article online and converts it into speech:

#Import the libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os

#Now after installing and importing the libraries, we need to get an article from online sources so that we can create a program to convert text to speech from that article:

#Get the article
article = Article('https://hackernoon.com/future-of-python-language-bright-or-dull-uv41u3xwx')

#Now, let’s download and parse the article:
article.download()
article.parse()

"""Now you need to download the “punkt” package if you have already downloaded it before you can skip downloading it if you will still download it again, it will give you a reminder that it is already available in your system which will not harm anything. So now, I will download the punkt package and apply Natural Language processing on it:"""

nltk.download('punkt')
article.nlp()

#Now, I will define a variable to store the article:

#Get the articles text
mytext = article.text

#Now we have to choose the language of speech. Note “en” means English. You can also use “pt-br” for Portuguese and there are others:

language = 'en' #English

#Now we need to pass the text and language to the engine to convert the text to speech and store it in a variable. Mark slow as False to tell the plug-in that the converted audio should be at high speed:

myobj = gTTS(text=mytext, lang=language, slow=False)

#Now, we have converted the article for text-to-speech, so now the next step is to save this speech to mp3 file:

myobj.save("read_article.mp3")

#Now let’s play the converted audio file from text to speech in Windows, using the Windows command “start” followed by the name of the mp3 file:

os.system("start read_article.mp3")
