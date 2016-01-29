#!/usr/bin/python
from math import *

def binom(n, k, p):
    q = 1 - p
    n_k = factorial(n)/(factorial(n-k)*factorial(k))
    p = n_k*(p**k)*(q**(n-k))
    return p

def indc(haploid_set):
    n = 2 * haploid_set
    p = 0.5
    result = []
    P = 0
    for k in range(n):
        P += binom(n, k, p)
        print P
        result.insert(0, log10(P))
    return result


for p in indc(5):
    print p,