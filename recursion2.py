
#base case - terminating condition that stops the function once it is met
#recursive case - breaking down the problem into smaller parts

#4! = 4 * 3 * 2 * 1
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

factorial_number = 4
print(factorial(factorial_number))

#1, 1, 2, 3, 5, 8

l = [2, 4, 6, 7]
def sum_list(li):
    if li == []:
        return 0
    else:
        return li[0] + sum_list(li[1:])

print(sum_list(l))
'''       
sum = 0
for letter in l:
    sum = sum + letter
'''

#1, 1, 2, 3, 5, 8, 13, etc

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))
