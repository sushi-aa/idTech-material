

def sumNumbers(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + sumNumbers(nums[ 1 : ])


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)




listofnumbers = [1, 2, 3, 4, 5]
print ( sumNumbers(listofnumbers) )
print( factorial(4) )


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print ( fib(5) )

