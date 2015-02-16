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
    
def convert_to_plottable(x,y,rows,columns):
    length=len(x)
    
    range_x=sorted(x)[-1]-sorted(x)[0]
    range_y=sorted(y)[-1]-sorted(y)[0]
    
    expand_x=float(columns)/range_x
    expand_y=float(rows)/range_y
    
    print expand_x
    print expand_y
    
    matrix=return_matrix(rows,columns)
    
    print y
    x_min=sorted(x)[0]
    y_min=sorted(y)[0]
    if(x_min<0):
        for i in range(0,length):
            x[i]=x[i]+abs(x_min)
    if(y_min<0):
        for i in range(0,length):
            y[i]=y[i]+abs(y_min)
 
    print y
    for i in range(0,length):
        index_x=int(round(x[i]*expand_x))
        index_y=int(round(y[i]*expand_y))        
        if(index_x>=columns):
            index_x=columns-1
        if(index_y>=rows):
            index_y=rows-1
        matrix[rows-1-index_y][index_x]=1
    return matrix
    
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
    
    matrix=convert_to_plottable(x,y,rows,columns)
    plot_matrix(matrix)
    
if(__name__=="__main__"):
    rows=30
    columns=80
    x=range(0,columns)
    y=[]
    for i in x:
        y.append(math.sin(2*math.pi*i/columns))
    text_plot(x,y,rows,columns)
    
    
    
