


list_to_sum = [2, 4, 3, 5, 8]

def find_sum(list_to_sum):
    if len(list_to_sum) == 0:
        return 0
    else:
        return list_to_sum[0] + find_sum(list_to_sum[1:])

print(find_sum(list_to_sum))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))



def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))




'''
for loops
lists: a = [1, 2, 3, 4]
nested for loops
****
***
**
*
a[2] means the 3rd element of the list
tuples: a = ("Dawon", 13, "something")
user input: user_guess = input("prompt")
if/else/elif statements
method definitions: def functionName() 
hangman game used a lot of these concepts
    random library 
    lists
while True
recursion
'''

a = [15, 16, 17]
#indexing starts at 0
print(a[2])

def functionName():
    print("we made a function")

user_number = input("Please enter a number: ")
review_tuple = ("Dawon", "blue", user_number)
print(review_tuple)

def review_recursion(parameter_list):
    if len(parameter_list) == 0:
        return 0
    else:
        return review_recursion(parameter_list[1:]) + parameter_list[0]

'''
variables
if/else statements
for loops
nested for loops
user input
method declarations/parameters
recursion
turtle library
'''

name = "Dawon" #strings represented in quotes
my_age = 18 #no quotes for integers
bool1 = True
bool1 = not bool1
print(bool1) #now False

for x in range(0, 5):
    for y in range(0, 3):
        print(x, y)


for i in range(0, 5):
    for j in range(0, i):
        print('* ', end="")
    print()