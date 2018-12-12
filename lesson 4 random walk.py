# Objectives:
# - Combine loops and logic with the turtle library
# - Combine loops and logic with the senseHat_emu
#
# ------------------------------------------------------ #
#
# Turtle Acticity:
# A random walk is a path traced by randomly moving in 1 of 4 directions
# Use the random and tutrle libraries to make a random walk

from random import *
from turtle import *

for i in range (10):
    r = randint(1,6)
    if r == 1:
        right(0)
    elif r == 2:
        right(60)
    elif r == 3:
        right(120)
    elif r == 4:
        right(180)
    elif r == 5:
        right(240)
    elif r == 6:
        right(300)
   
        
    forward(20)
