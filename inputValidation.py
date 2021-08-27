
# The program validates input.
age = ''
password = ''

# Keep asking for age until it is a number.
while not age.isdecimal():
    age = input('Enter your age: ')

# Keep asking for password until it consists of letters and numbers only.
while not password.isalnum():
    password = input('Enter the password: ')

# Welcome.
print('Well-come!')


