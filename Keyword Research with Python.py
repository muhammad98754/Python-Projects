"""I will use the Google API to access Google trends which can be done by using the pytrends library in python. Python being a general-purpose programming language provides libraries and packages for almost every task. pytrends can be easily installed by using the pip command – pip install pytrends"""
#You need to log in to Google first because, after all, we ask Google Trends for trending topics. For that, we need to import the method called TrendReq from the pytrends.request method:

import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

#Let’s see the terms that are popular in the region around the world. I will choose the term to search for as “Data Science”:

trends.build_payload(kw_list=["Data Science"])
data = trends.interest_by_region()
print(data.sample(10)
      
#Values are calculated on a scale of 0 to 100, where 100 is the most popular location as a fraction of the total searches for that location, a value of 50 indicates a location half as popular. Now let’s visualize the above search results to get better insights:

df = data.sample(15)
df.reset_index().plot(x="geoName", y="Data Science", figsize=(120,16), kind="bar")
plt.show()
      
#Now let’s take a look at the top daily search trends around the world. To do this, we need to use the trending_searches () method:

data = trends.trending_searches(pn="india")
print(data.head(10))
      
#Now, let’s see how we can get the google keywords suggestion for keyword research with python. Keywords are those words that are mostly typed by users in the search engine to find about a particular topic:

keyword = trends.suggestions(keyword="Programming")
data = pd.DataFrame(keyword)
print(data.head())
      
