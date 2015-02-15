#!/usr/bin/env python
import gcd
def test_gcd():
    flag=0
    assert gcd.gcd(2,40)==2, "Function doesn't give GCD of 2 and 40 as 2"
    assert gcd.gcd(19,35)==1, "Function doesn't give GCD of 19 and 35 as 1"
    try:
        trash=gcd.gcd(2,-700)
        print "Failed to raise ValueError for negative input"
        flag=1
    except ValueError:
        pass
    try:
        trash=gcd.gcd(2,700.3)
        print "Failed to raise TypeError for float value"
        flag=1
    except TypeError:
        pass
    if(flag==0):
        print "All good"
    else:
        print "At least one test failed"
        
if(__name__=="__main__"):
    test_gcd()
