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
    
def plot_matrix(matrix,test=0):
    rows=len(matrix)
    columns=len(matrix[0])
    if(test==1):
        test_build=""
    for i in range(0,rows):
        build=""
        for j in range(0,columns):
            if(matrix[i][j]):
                build=build+"*"
            else:
                build=build+" "
        if(test==0):
            print build
        elif(test==1):
            test_build=test_build+build
    if(test==1):
        return(test_build)
        
    

