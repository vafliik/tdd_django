from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(2)
	
	def tearDown(self):
		self.browser.quit()

	def test_todo_list_visible(self):
		#Ramirez heard about our great site, so he enters the address to browser
		self.browser.get('http://localhost:8000')
		#He notices the To-Do in browser title and he likes that
		self.assertIn('To-Do',self.browser.title)

		#The site has this tempting imput box, so he tries entering
		#his first to-do item "Buy soap"
		

		#The list nowcontains first item: "1. Buy soap" and Ramirez is happy
		
		self.fail('Stop the test for now ...')		

if __name__ == '__main__':
	unittest.main()

