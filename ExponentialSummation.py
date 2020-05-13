# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:56:16 2020

@author: skyle
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def exp(x, n):
    term = 0.0
    flag = 1
    if x < 0:
        flag = 0
        x = abs(x)
    for i in range(n+1):
        term = term + ((x**(i))/factorial(i))
    if flag==1:
        return term
    else:
        return 1/term

def factorial(k):
    value = 1.0
    for i in range (1, k+1):
        value = value*i
    return value
    
x = float(input("Enter an x value: "))
n = int(input("Enter the number of terms in your summation: "))

RelativeError = np.zeros(n)
Nterm = np.zeros(n)

for N in range (0, n):
    RelativeError[N] = abs((exp(x, N)-exp(x, N-1))/exp(x, N)) 
    Nterm[N] = N
    N +=1
    
for N in range (0, n):   
    print(Nterm[N], RelativeError[N])

plt.xlabel("N")
plt.ylabel("Relative error (E)")
plt.plot(Nterm, RelativeError, "o")
plt.show()

print("Your approximation of the exponential function is: ", exp(x,n))
print("The actual value of the exponential function is: ", math.exp(x))
