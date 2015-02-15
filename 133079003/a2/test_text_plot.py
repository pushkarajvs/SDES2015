#!/usr/bin/env python
import text_plot as tp
import math

def test_zeros():
    assert tp.zeros(5)==[0,0,0,0,0], "Not working for size=5"
    assert tp.zeros(1)==[0], "Not working for size=1"
    
def test_plot_matrix():
    rows=30
    columns=40
    matrix=tp.return_matrix(rows,columns)
    matrix[2][3]=1
    matrix[29][0]=1
    plot=tp.plot_matrix(matrix,1)
    for i in range(0,rows):
        for j in range(0,columns):
            assert ((matrix[i][j]==0 and plot[i*columns+j]==" ") or (matrix[i][j]==1 and plot[i*columns+j]=="*")), "Plot not correct"
          
          
if(__name__=="__main__"):
    test_zeros()
    test_plot_matrix()
