#!/usr/bin/env python
import unittest
import text_plot as tp

class Test_text_plot_oop(unittest.TestCase):
    def setUp(self):
      	self.rows=40
	self.columns=40
        self.test_matrix=tp.matrix(self.rows,self.columns)
   
    def tearDown(self):
      	del self.rows
	del self.columns
	del self.test_matrix

    def test_plot_matrix(self):
    	self.test_matrix.matrix[2][3]=1
    	self.test_matrix.matrix[29][0]=1
    	plotted=self.test_matrix.plot_matrix(1)
    	for i in range(0,self.rows):
            for j in range(0,self.columns):
            	self.assertTrue((self.test_matrix.matrix[i][j]==0 and plotted[i*self.test_matrix.columns+j]==" ") or (self.test_matrix.matrix[i][j]==1 and plotted[i*self.test_matrix.columns+j]==self.test_matrix.marker))
	
    def test_set_no_of_rows(self):
      	self.test_matrix.set_no_of_rows(50)
	self.assertEqual(self.test_matrix.rows,50)
      	self.test_matrix.set_no_of_rows(100)
	self.assertEqual(self.test_matrix.rows,100)

    def test_set_no_of_columns(self):
      	self.test_matrix.set_no_of_columns(50)
	self.assertEqual(self.test_matrix.columns,50)
      	self.test_matrix.set_no_of_columns(100)
	self.assertEqual(self.test_matrix.columns,100)

    def test__already_plotted(self):
      	self.test_matrix.plot_matrix(1)
	self.assertEqual(self.test_matrix._already_plotted(),1)

    def test_set_marker(self):
      	self.test_matrix.set_marker('+')
	self.test_matrix.make_plottable(range(0,10),range(0,10))
	mymatrix=self.test_matrix.plot_matrix(1)
	for i in range(0,self.test_matrix.rows):
	    for j in range(0,self.test_matrix.columns):
            	self.assertTrue(mymatrix[i*self.test_matrix.columns+j]==" " or mymatrix[i*self.test_matrix.columns+j]=="+")

    def test_get_no_of_rows(self):
      	self.test_matrix.rows=80
	self.assertEqual(self.test_matrix.get_no_of_rows(),80)

    def test_get_no_of_columns(self):
      	self.test_matrix.columns=80
	self.assertEqual(self.test_matrix.get_no_of_columns(),80)
	
class Test_plot(unittest.TestCase):
  	
    def test_plot(self):
    	mymatrix=tp.plot([1,2,3,4],[1,2,3,4],80,80,1)
	#print mymatrix
    	flag1=0
    	for i in range(0,15):
            for j in range(0,15):
            	if(mymatrix[i][79-j]==1):
                    flag1=flag1+1
            	if(mymatrix[79-i][j]==1):
                    flag1=flag1+1
	self.assertGreaterEqual(flag1,1)
    	mymatrix=tp.plot([300,400,500],[90000,160000,250000],40,40,1)
    	flag1=0
    	for i in range(0,5):
            for j in range(0,5):
                if(mymatrix[i][39-j]==1):
                    flag1=flag1+1    
                if(mymatrix[39-i][j]==1):
                    flag1=flag1+1
            	else:
                    continue
    	self.assertGreaterEqual(flag1,1)
	self.assertRaises(TypeError,tp.plot,[10,20,30],"a string",40,40,1)
	self.assertRaises(TypeError,tp.plot,[10,20,30],[20,30,40],40.1,50,1)
	self.assertRaises(ValueError,tp.plot,[10,20,30],[20,30,40,50],30,40,1)
	
    def test_zeros(self):
        self.assertEqual(tp.zeros(5),[0,0,0,0,0])
        self.assertEqual(tp.zeros(1),[0])

if(__name__=="__main__"):
    unittest.main()

