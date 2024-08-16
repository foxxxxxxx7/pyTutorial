email = input("Enter your email: ")

index = email.index("@") # remove this and follow comments below for less lines of code

username = email[:index] #domain = email[email.index("@") + 1:]
domain = email[index + 1:]  #username = email[:email.index("@")]

print(f"your username id {username} and domain is {domain}")