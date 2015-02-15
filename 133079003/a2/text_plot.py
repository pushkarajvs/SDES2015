#!/usr/bin/env python
"""
    
"""
import math

def zeros(size):
    allzeros=[]
    for i in range(0,size):
        allzeros.append(0)
    return allzeros

def return_matrix(rows,columns):
    matrix=[]
    for i in range(0,rows):
        matrix.append(zeros(columns))
    return matrix
