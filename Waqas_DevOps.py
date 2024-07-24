# Get the username and password from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Print out the username and password
print("Username:", username)
print("Password:", password)

import getpass

# Get the username and password from the user
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

# Print out the username (but not the password for security reasons)
print("Username:", username)
print("name:")
print("hello world,zeeshan ")