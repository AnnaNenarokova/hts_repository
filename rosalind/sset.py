#!/usr/bin/python
from math import *

def combination(n, k):
    C_n_k = factorial(n)/(factorial(n-k)*factorial(k))
    return C_n_k

def sset(n):
    sset_sum = 0
    for k in range(n+1):
        sset_sum += combination(n, k)
    return sset_sum


n = 810
result = sset(n) % 1000000

print result