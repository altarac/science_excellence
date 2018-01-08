# Obejctives:
# In this lesson, we will learn about:
# - Comments
# - Variables
# - Strings (i.e. text)
# - the print() function
# - the input() function
# - some basic math

# -------------------------------------------- #

# Comments
# the "hash-tag" # symbol is used to turn text into a comment. Without the hash-tag, the computer witll try to run the code but an error will occur.

# -------------------------------------------- #

# Variables
# in computer science, variables are things that store information to be used later. for example:

a = 10 # Here, the letter a is a variable storing the number 10.
# We can use the variable later instead of the number. For example:

a + 5 # This takes the value of a which is 10 and adds 5 to it.
# The result should be 15. If we print the result to the screen we will see if this is correct.

# -------------------------------------------- #

# The print() function:
# Let's print the result of the above addition to our screens. Remember, a was 10 and we added 5 so the result should be 15

print(a+5)
# Here we are telling the computer to put the result of a+5 on the screen.


# Try printing other things to the screen like print(a) or print(20-a)

# -------------------------------------------- #

# Strings
# A string is a like of text. like 'hello world'.
# Notice that there are quotes around hello world. This tells the computer that it is reading text. We can print text to the screen like this:

print('hello world')

# we can store text in a variable also like:
w = 'hello everyone'
# Now what happens if we print the variale w? Try it: print(w)

# -------------------------------------------- #

# The input() function
# Lets make our program a little bit more interactive.
# we can ask the user to give us information with the input() function. Don't forget to store the info in a variable otherwise the computer will forget what the user said!

x = input('What is your name? ')
# Here the computer will stop running the program and wait for the user to input something. The string 'what is your' name shows up on the screen. Once the user inputs something the answer gets stored in the variable x.

# can use that answer later. For example we can print it to the screen like this:

print(x)

# -------------------------------------------- #

# Basic math
# Python can do all kinds of math for us. Lets start by learning the basics: adding +, subtracting - , multiplying *, dividing /, exponents **  (it knows how to respect BEDMAS).

ans = (2+3)**2-5
# Here, we are adding 2 and three then squaring the result then subtracting 5 and storing it in the variable ans. What do you think we get if we print the answer to the screen? Try it ptint(ans).

# -------------------------------------------- #

# Challenge:
# Write a small program that askes the user for their age and takes the average of their age and the teacher's age (use 30 if the teachers won't to tell you their age). Don't forget to print() the answer to the screen.
