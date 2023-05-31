#To scrape useful information from Wikipedia, you need to install a package named as wikipedia, which can be easily installed using the pip command- pip install wikipedia
import wikipedia as wiki

#To explain the use of this package, I will scrape information based on Python. So let’s start with the task to scrape Wikipedia articles. The code below will get all the search suggestions of our input. In our case, it will return the search suggestions of Python:

print(wiki.search("Python"))

#Now let’s see will the search engine on Wikipedia suggest us python if we will type only some alphabets of its spelling:

print(wiki.suggest("Pyth"))

#Yes, it works, now let’s have a look how we can get the summary of an article on Wikipedia:

print(wiki.summary("Python"))


#If you want to read the summary in another language other than English, we can also do that. I will get the same summary above in the French language:

wiki.set_lang("fr")
print(wiki.summary("Python"))

#Now let’s change the language back to English and have a look at some more insights from the article. Here I will scrape all the information we will get if we will read about python on Wikipedia:

wiki.set_lang("en")
p = wiki.page("Python")

#To get the Title:

print(p.title)

#To get the url of the article:

print(p.url)

#To scrape the full article:

print(p.content)

#To get all the images in the article:

print(p.images)

#And to get all the referals used by Wikipedia in the article:

print(p.links)

