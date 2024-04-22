import sys
sys.setrecursionlimit(100000)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
        
print('factorial(5):', factorial(5))
# Expected 120

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 2) + fib(n - 1)

print('fib(8):', fib(8))
# Expected 13

def addup(list):
    if len(list) == 0:
        return 0
    return list[0] + addup(list[1:])

print('addup([1,2,3,4,5]):', addup([1,2,3,4,5]))
# Expected 15

print('addup(range(101)):', addup(range(101)))
# Expected 5050
