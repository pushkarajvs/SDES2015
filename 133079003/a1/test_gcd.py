#!/usr/bin/env python
import gcd
def test_gcd():
    assert gcd.gcd(2,40)==2, "Function doesn't give GCD of 2 and 40 as 2"
    assert gcd.gcd(19,35)==1, "Function doesn't give GCD of 19 and 35 as 1"
    
if(__name__=="__main__"):
    test_gcd()
