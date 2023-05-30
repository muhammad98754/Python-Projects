email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)

""" We take user input and use the strip function at the same time to remove white space if any. 
Then we are finding the index of ‘@’ symbol of the user input. 
Then we store the index into a variable known as domain_name to split the email into two parts; the user name and the domain."""
