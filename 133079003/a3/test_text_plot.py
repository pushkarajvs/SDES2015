#!/usr/bin/env python
import unittest
import text_plot as tp

class Test_text_plot(unittest.TestCase):
    def setUp(self):
        self.seq=range(10)
    def test_zeros(self):
        self.assertEqual(tp.zeros(5),[0,0,0,0,0])
        self.assertEqual(tp.zeros(1),[0])

if(__name__=="__main__"):
    unittest.main()

