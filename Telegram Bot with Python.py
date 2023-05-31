"""A bot is a software application programmed to perform certain tasks. The robots are automated, which means that they operate according to their instructions without a human user needing to start them. Bots often mimic or replace the behaviour of a human user. """

"""To create a Telegram Bot using Python, you need to go through some steps to get a telegram bot API from the BotFather account on Telegram. BotFather is simply s Bot which helps in creating more bots by providing a unique API. So before using python to create our Telegram bot, we need to go through some steps to get the API."""
"""First, create an account on telegram if you don’t have an account. After making your account search for BotFather, which is an official telegram bot that provides API to create more bots. When you will open the chat just write /start and send. The BatFather will reply you with a long text without reading the text you can type Newbot.

Now it will reply you again with a long text, asking about a good name for you Telegram bot. You can write any name on it. Now the next step is to give a username to your bot which should be in a format Namebot or Name_bot. And the main thing to notice in this step is that your username should be a unique one, it should not match any other username all around the world.
Now after typing a unique username, it will send you an API key between a long message, you need to copy that username and get started with Python."""

"""Now, we have the API key to build our telegram bot, the next step is to install a package known as telegram, which can be easily installed by using the pip command in your command prompt or terminal – pip install python-telegram-bot.

After successfully installing the package, now let’s import the required packages and get started to make a Telegram Bot with Python. We only need the telegram package for this task, I will import it and prepare our program to read our API Key:"""

import telegram
bot = telegram.bot(token='TOKEN') #Replace TOKEN with your token string

#Now that everything is working, let’s follow the tradition and create a Hello World program. I will simply program our chatbot here with a command on which our telegram bot will respond with the message “Hello, World”:

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='TOKEN', use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher

#Now let’s create a hello function that sends the desired text message through the bot:

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')
    
#We now use a CommandHandler and register it in the dispatcher. Basically, we bind the / hello command with the hello () function:

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)
#And that’s it. To start our bot, add this code at the end of the file:

updater.start_polling()


#covid 19 Telegram Bot

#Now, let’s build our program to get information related to the COVID-19 to get results from a simple text. Now here, you need to import two modules here known as requests and json. Now let’s import these two modules and build a COVID-19 telegram Bot with Python:

import requests
import json
def summary(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code==200): #Everything went okay, we have the data
        data = response.json()
        print(data['Global'])
        context.bot.send_message(chat_id=update.effective_chat.id, text=data['Global'])
    else: #something went wrong
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")
corona_summary_handler = CommandHandler('summary', summary)
dispatcher.add_handler(corona_summary_handler)

