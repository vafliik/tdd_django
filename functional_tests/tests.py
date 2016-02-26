from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(2)
	
	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, expected_row):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')

		self.assertIn(expected_row, [row.text for row in rows])
		

	def test_todo_list_visible(self):
		#Ramirez heard about our great site, so he enters the address to browser
		self.browser.get(self.live_server_url)
		#He notices the To-Do in browser title and he likes that
		#Also the heading is there, so Ramirez knows heis on the right track
		self.assertIn('To-Do',self.browser.title)
		heading = self.browser.find_element_by_tag_name('h1')
		self.assertIn('To-Do',heading.text)

		#The site has this tempting imput box, so he tries entering
		#his first to-do item "Buy soap"
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

		inputbox.send_keys('Buy soap')

		#When he hits Enter, the item is sent.
		#The list now contains first item: "1. Buy soap" and Ramirez is happy
		inputbox.send_keys(Keys.ENTER)
		
		self.check_for_row_in_list_table('1. Buy soap')
		
		#There is still this lovely input field, so Ramirez imediatelly continues
		#entering his items. The next one is "Have a bath"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Have a bath')
		inputbox.send_keys(Keys.ENTER)

		#The table with to-dos is updated again, displaying the new item as next
		self.check_for_row_in_list_table('2. Have a bath')
		self.check_for_row_in_list_table('1. Buy soap')

		#Ramirez has his list on unique URL
		ramirez_list_url = self.browser.current_url
		self.assertRegex(ramirez_list_url, '/lists/.+')
		
		#Now Juanita at the other side of village comes to her PC and wants to check this
		#TO DO list page that she heard about in zapateria

		##Use new browser session
		self.browser.quit()
		self.browser = webdriver.Firefox()

		#Juanita visits home page. Ramirez's list is not there of course
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Have a bath',page_text)
		self.assertNotIn('Buy soap',page_text)
	
		#Juanita starts a new list by entering new item
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy new shoes')
		inputbox.send_keys(Keys.ENTER)
		
		#Juanita gets her own list URL
		juanita_list_url = self.browser.current_url
		self.assertRegex(juanita_list_url, '/lists/.+')
		self.assertNotEqual(juanita_list_url,ramirez_list_url)

		#After the list iscreated, there is no traceof Ramirez's list
		page_text = sel.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Have a bath',page_text)
		self.assertNotIn('Buy soap',page_text)

		#They are both satisfied

		self.fail('We are not finished with the test yet ...')		

if __name__ == '__main__':
	unittest.main(warnings='ignore')

