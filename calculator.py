import numpy as np
def add(x, y):
    return x+y

def factorial(x):
    input = x
    fact = 1
    if input < 0:
        raise ValueError("The input must be positive")
    else:
        for i in range(1,input + 1):
            fact = fact * i
    return fact

def sin(x, N):
    num = 0
    for n in range(0, N+1):
        num = num + ((-1)**n * x**(2*n + 1) / factorial(2*n+1))                 #Note this function needs the function factorial to run
    return num

def divide(x,y):
    return x/y

def subtract(x,y):
    return x-y

def times(x, y):
    return x*y
