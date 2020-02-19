# Objectives:
# We will learn how to import and use code other people have written for us like:
# - Random
# - Turtle
# - SenseHat_emu

# ---------------------------------------------------- #

# The trick here is to use google a lot to see how other people have used the code you are trying to import. Don't be shy to google your question!

# There is a python file called 'random' that lets you get a random number.
# Let's make a small program that gives us a random number bewteen 1 and 6 like dice...

import random
# this lets us import the file math where we can find the random number generator.

rand_number = random.randint(1, 6)
print(rand_number)
# Here we are getting a random integer by using a function called randint() and we are storing that number in a variable called rand_number. The random number will be between 1 and 6. Finally, we print the variable rand_number to the screen.

# Try making the program generate random numbers between 1 and 20 like a dungeons and dragons dice.

# ------------------------------------------ #

# Turtle
# Python also comes with other files that let you make drawings. A basic program we can use is called 'tutrle'. Let's import it and start making some simple art.

from turtle import *
# Here we are saying we want to use all (*) the functions found int the file called turtle. The following code now draws a staright like 100 pixels long.

forward(100)
# Normally we cannot just say forward(100). The computer doesn't know what that means but we can use it here because the forward() function is in the turtle file and by importing that file we told the computer what forward() means.

# we can also make the turtle (little triangle on the screen) turn left or right. Let's darw a triangle:

forward(100)
left(120)
forward(100)
left(120)
forward(100)

# Challenge:
# What does 120 mean in the left() function?
# Can you make other shapes?

# ------------------------------------------ #

# SenseHat_emu
# Do not pluf in sense hat if the Pi is also plugged in.
# The Raspberry Pi can be connected to a SenseHat. This let's it sense things in its environment like: temperature, pressure, humidity, acceleration, and more...
# If you don't have a SenseHat you can use the emulator by importing it like this:

from sense_emu import SenseHat

# now we can get readings of humidity or temperature from the emulator like this:
sense = SenseHat()
# This stores the SenseHat() family of functions in the variable sense
h = sense.humidity # gets us the the humidity reading and stores it in the variable h

print(h) # this prints to the screen the humidity stored in the variable h.

# go to http://sense-emu.readthedocs.io/en/v1.0/examples.html#humidity to get other examples of code
# Challenge:
# Can you make the room temperature scroll across the SenseHat LED matrix?
