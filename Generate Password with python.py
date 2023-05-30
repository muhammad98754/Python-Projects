import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)
"""first imported the random module in Python, then I asked for user input for the length of the password.
Then I stored the letters, numbers and special characters that I want to be considered while generating a password.
Then I am doing a random sampling by joining the length of the password and the variable s, which will finally generate a random password."""
