import unittest
import simple_one

class TestCap(unittest.TestCase): #inherit unittest.TestCase

	def test_one_word(self):
		text='python'
		result=simple_one.cap_text(text)
		self.assertEqual(result,'Python')
    
if __name__=='__main__':
	unittest.main() 
