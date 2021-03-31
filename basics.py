

#comments
#printing
#variables and data types
#if statements

print("Hello!")
#variable
#name of the variable = value of the variable
name = "Arushi"
age = 19

print(name) #--> Arushi #print("name") --> name

#Hello, my name is Arushi and I am 19 years old.
print("Hello, my name is " + name + " and I am " + str(age) + " years old.")

#integer is basically a number
#string is a word or a sentence
#boolean is a type of variable that can only have 2 possible values
    # either or true or false

#if statement, else statement

if age > 18:
    print("You are an adult")
else:
   print("You are not an adult")

'''   
define an integer variable called socks 
use an if-else statement to print "You have too many socks" if socks > 15, or "You don't have enough socks" if 
socks < 10 
'''

#15

if age > 18:
    print("You're an adult")
elif age > 13:
    print("You're a teen")
else:
    print("You're neither")

is_adult = False #is_adult = False
if (is_adult):
    print("You're over 18")
else:
    print("You're under 18")

#double equals means comparison, single equals means assignment
if name == "Arushi":
    print("You are teaching a lesson")
elif name == "Sonia":
    print("You are the student")
else:
    print("You are not in this lesson.")



