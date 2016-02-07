from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):

	def test_home_page_contains_todo_list(self):
		request = HttpRequest()
		response = home_page(request)
		expected_content = render_to_string('home.html',request=request)
		#use decode to compare byte with string
		self.assertEqual(response.content.decode(), expected_content)
		
	def test_home_page_shows_items_from_db(self):
		Item.objects.create(text='Item 1')
		Item.objects.create(text='Item 2')

		request = HttpRequest()
		response = home_page(request)
		
		self.assertIn('Item 1', response.content.decode())
		self.assertIn('Item 2', response.content.decode())

	def test_home_page_can_save_post_requests_to_db(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'New item'
		
		response = home_page(request)
		
		item_from_db = Item.objects.all()[0]
		self.assertEqual(item_from_db.text, 'New item')
		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['Location'], '/')

from lists.models import Item
class ItemModelTest(TestCase):

	def test_saving_and_retrieving_from_db(self):
		first_item = Item()
		first_item.text = 'Very first item'
		first_item.save() 
		
		second_item = Item()
		second_item.text = 'The second item'
		second_item.save()

		first_item_from_db = Item.objects.all()[0]
		self.assertEqual(first_item_from_db.text, 'Very first item')

		second_item_from_db = Item.objects.all()[1]
		self.assertEqual(second_item_from_db.text, 'The second item')
 
