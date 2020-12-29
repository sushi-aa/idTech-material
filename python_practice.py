'''
variables, printing, comments
user input
for loops, if/elif/else
teach exceptions, try-except-else-finally blocks?
lists
teach recursion
teach classes
list comprehensions
teach tuples, lists, sets, dictionaries
    #https://www.ics.uci.edu/~thornton/ics32/Notes/TuplesAndLists/
    #https://www.ics.uci.edu/~thornton/ics32/Notes/SetsAndDictionaries/
check pattis notes/projects
teach file directories, etc
'''


#practice with if/else statements
#writing code to check whether a user inputted character is a vowel or consonant

'''
s = {1, 2, 3}
print(s)
print(1 in s)
print(20 in s)

s2 = {3, 4, 5, 6}
print(s | s2)
print(s & s2)

for x in s2:
    print(x)

print(list(s))

t = ('Arushi', 18, 'dog')

print(len(t))
#print(t[0], t[1], t[2])

#sequential assignment
x, y, z = t
print(x, y, z)


#program for Cassia's birthday
print("Welcome to Mireya's MindReader™ ")
shrek = input("Do you like Shrek? yes or no ")
if shrek == 'no' or shrek == "No":
    print("You must be an imposter -- Cassia loves Shrek! ")
elif shrek == "yes" or shrek == "Yes":
    d = {'Cassia': {'favorite color': 'purple', 'age': 15, 'favorite animal': 'cat', 'sibling 1': 'Mireya', 'sibling 2': 'Kellan'}}

    name = ''
    color = ''
    age = 0
    animal = ''
    sib1 = ''
    sib2 = ''
    for key, value in d.items():
        name = key
        color = value['favorite color']
        age = value['age']
        animal = value['favorite animal']
        sib1 = value['sibling 1']
        sib2 = value['sibling 2']

    print('\nI feel like your name is... ' + name + ' \nyour favorite color is ' + color + ' \nyour age is ' + str(age)
          + ' \nyour favorite animal is a ' + animal + ' \nyou have 2 siblings named ' + sib1 + ' and ' + sib2)



d = dict()
d['india'] = 'blue'
d['arushi'] = 'purple'
d['luca'] = 'plain'

print(d.keys())
print(d['arushi'])

name = ['i', 'n', 'd', 'i', 'a']
name.reverse()
print(name)
#d[['india'].reverse()] = 'blue'


#print( sorted(d.items()) )

d2 = {'age':18, 'favorite animal': 'dog'}
d2.update({'favorite color': 'purple'})

print(d2)
print('favorite animal' in d2)

d3 = {'number1': 10, 'number2' : 20, 'number3':15}


#del d3['number4']
#print(d3)

d4 = dict()
for i in range(0, 10):
    d4[i] = i**2

print(d4)


print( sorted(d3.items(), key=lambda x: x[1]) )

'''

d = dict()
d1 = {'sahil': 'red', 'neel':'blue'}
print(d1)

print(d1.keys())
for key, value in d1.items():
    print(key)
    print(value)

d1.update({'Arushi':'orange'})
print(d1)

d2 = dict()
for i in range(0, 10):
    d2[i] = i**2

print(d2)

set1 = {3, 4, 5, 10, 5}
print(set1)
#print(set1[0])

tuple2 = ('Sahil', 'Neel', 15, 20)
print(tuple2)































