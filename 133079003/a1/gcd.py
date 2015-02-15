#!/usr/bin/env python
"Contains a function to calculate GCD (Greatest Common Divisor) of two numbers"
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
