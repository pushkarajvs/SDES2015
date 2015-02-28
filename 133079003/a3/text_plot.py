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

def create_matrix(rows,columns):
    """
    Returns a matrix list of zeros of size (rows,columns)
    """
    matrix=[]
    for i in range(0,rows):
        matrix.append(zeros(columns))
    return matrix

class matrix(object):
    """
    A class for the canvas to draw upon
    """
    def __init__(self,rows=30,columns=80):
        self.rows=rows
        self.columns=columns
        self.matrix=create_matrix(self.rows,self.columns)
        self._busy=0

    def get_no_of_rows(self):
      	"""
	Returns current number of rows of the matrix
	"""
        return self.rows

    def get_no_of_columns(self):
      	"""
	Return current number of columns of the matrix
	"""
      	return self.columns

    def plot_matrix(self,test=0):
        """
        Plots the matrix created during the initialization based on its non-zero entries. The matrix should contain 1's only where the points are to be plotted. Rest all should be zeros.
        """
    	if(test==1):
            test_build=""
    	for i in range(0,self.rows):
            build=""
            for j in range(0,self.columns):
            	if(self.matrix[i][j]):
                    build=build+"*"
            	else:
                    build=build+" "
	    if(test==0):
            	print build
            elif(test==1):
            	test_build=test_build+build
	self._busy=1
    	if(test==1):
            return(test_build)

    def make_plottable(self,x,y):
        """
        Converts 2 user entered lists as x and y indices into ready to plot matrix by considering the total size of the plot available and expanding or contracting the scale accordingly.
        """
    	length=len(x)
    
    	range_x=max(x)-min(x)
    	range_y=max(y)-min(y)
    
    	expand_x=float(self.columns)/range_x
    	expand_y=float(self.rows)/range_y
    
    	x_min=min(x)
    	y_min=min(y)
    	if(x_min<0):
            for i in range(0,length):
            	x[i]=x[i]+abs(x_min)
    	if(y_min<0):
       	    for i in range(0,length):
            	y[i]=y[i]+abs(y_min)
 
    	for i in range(0,length):
            index_x=int(round(x[i]*expand_x))
            index_y=int(round(y[i]*expand_y))        
            if(index_x>=self.columns):
            	index_x=self.columns-1
            if(index_y>=self.rows):
            	index_y=self.rows-1
            self.matrix[self.rows-1-index_y][index_x]=1

    def _already_plotted(self):
      	"""
	Returns 'True' if a matrix is already filled with values and plotted.
	"""
      	return self._busy

    def _change_size(self,new_rows,new_columns):
      	"""
	Resizes the matrix according to new number of rows and columns.
	Bug: When resized to very small sizes in either dimension, expanding again results in a patchy plot due to rounding off.
	"""
	new_matrix=create_matrix(new_rows,new_columns)	
	resize_x=float(new_columns)/self.columns
	resize_y=float(new_rows)/self.rows
	for i in range(0,self.rows):
	    for j in range(0,self.columns):
	      	if(self.matrix[i][j]):
		    index_x=int(round((self.rows-1-i)*resize_y))
		    index_y=int(round(j*resize_x))
		    if(index_x>=new_rows):
		      	index_x=new_rows-1
		    if(index_y>=new_columns):
		      	index_y=new_columns-1
		    new_matrix[new_rows-1-index_x][index_y]=1
	self.matrix=new_matrix
	self.rows=new_rows
	self.columns=new_columns

    def set_size(self,rows,columns,refresh_plot=0):
      	"""
	Allows to resize the matrix from the size which was specified during initialization.
	If refresh_plot=1, then plots the resized matrix.
	"""
	if(self._already_plotted()):
	    self._change_size(rows,columns)
	    if(refresh_plot):
	      	self.plot_matrix()
	else:
       	    self.rows=rows
	    self.columns=columns
	    self.matrix=create_matrix(rows,columns)

def plot(x,y,rows=30,columns=80,test=0):
    """
    General text-based plotting function
    """
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
    
    my_matrix=matrix(rows,columns)
    my_matrix.make_plottable(x,y)
    
    if(test==0):
        my_matrix.plot_matrix()
    else:
        return(my_matrix)

if(__name__=="__main__"):
    rows=30
    columns=80
    x=range(0,columns)
    y=[]
    for i in x:
        y.append(math.sin(2*math.pi*i/columns))
    plot(x,y,rows,columns) 
