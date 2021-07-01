# This program says hello and asks for your name and age.

print('Hello!')
print('What is your name?') # ask for their name
Name = input() # string
print()

print('Welcome ' + Name + '! What is your age, if I may ask?') # ask for their age
Age = input() # string
print()

print(Name + ' so you are ' + Age + ' years old.')
print('That means that you will be ' + str(int(Age)+1) + ' years old next year.')
print('It was a pleasure to meet you ' + Name + '!')
print()

