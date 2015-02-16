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
          
def test_text_plot():
    matrix=tp.text_plot([1,2,3,4],[1,2,3,4],80,80,1)
    flag=0
    flag1=0
    for i in range(0,15):
        for j in range(0,15):
            if(matrix[i][79-j]==1):
                flag1=flag1+1    
            if(matrix[i][79-j]==1):
                flag1=flag1+1
    if(flag1<1):
        print "Function doesn't make use of the entire available range"
        flag=1
    #print flag1
    matrix=tp.text_plot([300,400,500],[90000,160000,250000],40,40,1)
    flag1=0
    for i in range(0,5):
        for j in range(0,5):
            if(matrix[i][39-j]==1):
                flag1=flag1+1    
            if(matrix[i][39-j]==1):
                flag1=flag1+1
            else:
                continue
    if(flag1<1):
        print "Function doesn't compress the range of input values effectively"
        flag=1
    return flag
    
        
if(__name__=="__main__"):
    test_zeros()
    test_plot_matrix()
    flag=test_text_plot()
    if(flag):
        print "At least one test failed"
    else:
        print "All good"
