
#lists
#tuples
#sets
#dictionaries
'''
y = []
x = [3, 4, 6, 8, 10, 12, 15, 14]
z = ["Roni", "Arushi", "Sahana"]

#indexing
print(len(x)) #length function

print("The element at index 3 is: " + str(x[3]))
print("The last element is: " + str(z[-1]))
print(x[-1])

#slicing
multiple_elements = x[1:4]
print(multiple_elements)
print(x[4])

print(x[0:])

every_other = x[0:8:3]
print(every_other)

# [start index: stop index: step value]

x.append(20)
print(x)
print(x[6:2:-1])

print(x[::-1])

#empty dictionary that will be filled later
d1 = dict()
'''

#dictionary that already has values
d2 = {"Roni": 12, "Sahana": 14, "Arushi": 18}
print(d2["Roni"])
print(d2["Sahana"])

#del d2["Arushi"]
#print(d2)

#in operator
print("Roni" in d2)
print("Arushi" in d2)
print("Sahana" in d2)


for key, value in d2.items():
    print(key, value)



print(d2.keys())
print(d2.values())

print(sum(d2.values()))


result = 1
for k in d2:
    result = result * d2[k]

print(result)

print(sorted(d2, reverse=True))

#takes 3 parameters: iterable object, key, reverse