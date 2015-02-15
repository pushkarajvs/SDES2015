#!/usr/bin/env python
"Contains a function to calculate GCD (Greatest Common Divisor) of two numbers"
def gcd(a, b):

    """
         Calculates GCD of two numbers
         Syntax - gcd(a, b)
         Both a and b should be either int or long.
    """
    
    if((type(a) != int and type(a) != long) or (type (b) != int and type(b) != long)):
        raise TypeError("Both values should be either an int or a long.")

    if(a <= 0 or b <= 0):
        raise ValueError("Both values should be positive.")
    
    while b:
        a, b = b, a % b
    return a
