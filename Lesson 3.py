# Objective:
# - Arrays; store many data points in 1 variable
# - if, elif, and else logic
# - For and While loops

# ---------------------------------------------------- #

# Arrays
# These are lists of values. The values are stored in square brackets
# and separated by a comma like this:

b = []
# This is an empty array stored in the varaible b

a = [1, 2.5, 'cat']
# This is an array with 3 element.
# the first element in an array is the zero-th element.
# if you want to print to the screen the number 1 that is stored in the array, you can refference it like this:

print(a[0])
# This says print to the screen the 0-th element in array called a.

print(a[2])
# This says print the element of array a that is in position 2. This happens to be the last position of a and it is the string 'cat'

# You can add more things to an array by using the append() function like this:

a.append('new element')
# This 'new element' is in position 3. To print it to the screen we do this:
print(a[3])

# Can you have the user input() 3 peices of information about themselves and store all that info in an array called user then print to the screen this information?

# ---------------------------------------------------- #

# If, elif, and else logic
# When you need your program to make a 'choice', we can verify a condition using an if/else statement.for example:

x = input('How old are you? ')
if x >= 18:
    print("You're old enough to drive")
else:
    print("You're not old enough to darive")


# Here, the code asks the user to input their age. This gets store in the variable x. Next the if statement checks if the number is greater than or equal to 18. If it is greater than it prints "You're old enough to drive" or else it will print "You're not old enough to darive".

# Now your code can make decisions.
# Challenge:
# Can you write a program to check if a number is even
# Hint: use the modulo (%) operation to see what is leftover after a division is made.

# ---------------------------------------------------- #

# For and While loops:
# If you need your code to repeat itself for a specific number of times,
# use the for loop like this:

for i in range(0, 5):
    print(i)
    print('hi')
# This says let the variable i take on the values between 0 and 5 (not including 5) and then print the value of i followed by printing 'hi' on the next line.

# you can make a program loop forever with a while loop like this:
while True:
    print('This is the song that never ends')

# This will print 'This is the song that never ends' forever since the while loop checks if the condition is true but the condition is set to True permanently. Press controll or command c to stop a runaway loop in the IDLE.

# Challenge:
# can you use a while loop to run a print statement 5 times?
