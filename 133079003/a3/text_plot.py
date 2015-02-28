#!/usr/bin/env python
"""
    A module for text-based plotting of an array of values against another array of values.
"""
import math

def zeros(size):
    """
    Returns a zero list of size length
    """
    allzeros=[]
    for i in range(0,size):
        allzeros.append(0)
    return allzeros

class matrix(object):
    """
    A class for the canvas to draw upon
    """
    def __init__(self,rows=30,columns=80):
       self.rows=rows
       self.columns=columns
       matrix=[] 
       for i in range(0,self.rows):
           matrix.append(zeros(self.columns))
       return matrix
