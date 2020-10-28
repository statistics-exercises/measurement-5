import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_exists(self) : 
        self.assertTrue( "xbar" in globals(), "The variable xbar is not defined" )
        
   def test_values(self) : 
       mmm = sum((4/3)*np.pi*radii*radii*radii)/len(radii)
       self.assertTrue( xbar==mmm, "xbar has not been calculated correctly" )
