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
        
def text_plot(x,y,rows=30,columns=80):
    counter=0
    for entry in x:
        if(type(entry)!=float and type(entry)!=int and type(entry)!=long):
            raise TypeError("All the input values should be numbers.")
        x[counter]=float(entry)
        counter=counter+1
    
    counter=0            
    for entry in y:
        if(type(entry)!=float and type(entry)!=int and type(entry)!=long):
            raise TypeError("All the input values should be numbers")
        y[counter]=float(entry)
        counter=counter+1
    
    if(type(rows)!=int and type(rows)!=long and type(columns)!=int and
            type(columns)!=long):
        raise ValueError("Number of rows and columns should be either int or long.")
    
    if(len(x)!=len(y)):
        raise ValueError("both input lists should be of the same size")
    
    x=list(x)
    y=list(y)
    
    matrix=return_matrix(rows,columns)
