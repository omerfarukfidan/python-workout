
from pdb import line_prefix


if 2<3:
    print("2 is less than 3")

# comment lines are making like that

"""
also this a comment line with more than one line
"""

# while you are creating a variable it needed to be assigned for example:

x="my name is omer" #now it is a string 
#also you can change the type of variable
x=2 #now x variable is a integer
#variables do not need to be declared with any particular type
print("_____________________________________________________")

#but anyway you want specify the data type of a variable, this can b e done with casting
x= str(3)
y= int(3)
z= float(3)

#you can get the data type by using type() function
print(type(x))
print(type(y))
print(type(z))

print("_____________________________________________________")

x, y, z = "blue", "white", "red"

print(x)
print(y)
print(z)

print("_____________________________________________________")

x = y = z = "blue"

print(x)
print(y)
print(z)

print("_____________________________________________________")

fruits = ["apple", "banana", "cherry"]
x, y, z= fruits
print(x)
print(y)
print(z)

print("_____________________________________________________")


x = "awesome"

print("Omer is " + x)

print("_____________________________________________________")

x = "Omer is "
y = "awesome"
z= x + y
print(z)

print("_____________________________________________________")

x = 5
y = 10
print(x+y)

print("_____________________________________________________")

x = "awesome"
def myFunc():
    print("Omer is " + x)

myFunc()

print("_____________________________________________________")

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print("_____________________________________________________")

import random
print(random.randrange(1,10)) # it creates random numbers 1 to 10

print("_____________________________________________________")

#three double quotes can be used while writing a paragraph
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print("_____________________________________________________")

sentence = "hello my name is omer"

print(sentence[3])