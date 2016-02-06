from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
		#Also the heading is there, so Ramirez knows heis on the right track
		self.assertIn('To-Do',self.browser.title)
		heading = self.browser.find_element_by_tag_name('h1')
		self.assertIn('To-Do',heading.text)

		#The site has this tempting imput box, so he tries entering
		#his first to-do item "Buy soap"
		inputbox = self.browser.find_element_by_id('id_new_iteem')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

		inputbox.send_keys('Buy soap')

		#When he hits Enter, the item is sent.
		#The list now contains first item: "1. Buy soap" and Ramirez is happy
		inputbox.send_keys(Keys.ENTER)
		
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')

		self.assertIn('1. Buy soap', [row.text for row in rows])
		
		#There is still this lovely input field, so Ramirez imediatelly continues
		#entering his items. The next one is "Have a bath"
		inputbox = self.browser.find_element_by_id('id_new_iteem')
		inputbox.send_keys('Have a bath')
		inputbox.send_keys(Keys.ENTER)

		#The table with to-dos is updated again, displaying the new item as next
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')

		self.assertIn('1. Buy soap', [row.text for row in rows])
		self.assertIn('2. Have a bath', [row.text for row in rows])

		self.fail('We are not finished with the test yet ...')		

if __name__ == '__main__':
	unittest.main()

