"""OTP Verification is the process of verifying a user by sending a unique password so that the user can be verified before completing a registration or payment process. Most of the time, we get an OTP when we make an online payment, or when we forget our password, or when creating an account on any online platform. Thus, the sole purpose of an OTP is to verify the identity of a user by sending a unique password.

We can easily create an application for the task of OTP verification using Python by following the steps mentioned below:

First, create a 6-digit random number
Then store the number in a variable
Then we need to write a program to send emails
When sending email, we need to use OTP as a message
Finally, we need to request two user inputs; first for the user’s email and then for the OTP that the user has received.
So this is the complete process of creating an OTP verification application using Python"""

#start by importing the necessary Python library that we need for this task:
import os
import math
import random
import smtplib

#generate a random number and store it in a variable which I will be using while sending emails to the users:

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp

#After you create your app password for your Gmail account you will get a key. Copy that key and paste in the code below to send emails for OTP verification using Python:

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your Gmail Account", "You app password")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
    
#Once you run this code you enter an email where you want to send an OTP and then enter the OTP that you have received in the email.

import os
import math
import random
import smtplib

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your Gmail Account", "You app password")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
