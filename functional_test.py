from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(2)
	
	def tearDown(self):
		self.browser.quit()

	def test_todo_list_visible(self):
		self.assertIn('To-Do',self.browser.title)

if __name__ == '__main__':
	unittest.main()

