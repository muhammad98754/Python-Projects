"""To scrap Instagram, we will use a library know as instaloader which provides us with an API for scraping Instagram. You can install this library by using the pip method in your terminal – pip install instaloader. """

#First of all, if you are learning Data Science then scraping Instagram will help you in getting the new trends of businesses, so that you can generate more leads and can reach out for your new potential customers. Now let’s start with scraping Instagram users profiles:

# Import the module
!pip install instaloader
import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'safeer123')

print(type(profile))

#Now let’s see how we can extract some valuable information from an Instagram profile:

print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)

#Now let’s see how you can log in to your Instagram profile using python:

# Login with username and password in the script
bot.login(user="your username",passwd="your password")

# Interactive login on terminal
bot.interactive_login("your username") # Asks for password in the terminal

#Scraping your followers and followees will help you in getting a list of their usernames, which you will require to do when you will work in a professional environment in the data science field:

# Retrieve the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]

# Retrieve the usernames of all followees
followees = [followee.username for followee in profile.get_followees()]
print(followers)

#Getting posts from any profile is easy in python. We just need to use get_posts(). I will this method on the profile of someone else. To download each post, we need to loop over the generator object using .download_post() method. Now let’s go through this:

# Load a new profile
profile = instaloader.Profile.from_username(bot.context, 'wwe')

# Get all posts in a generator object
posts = profile.get_posts()

# Iterate and download
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")

