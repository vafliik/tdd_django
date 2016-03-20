from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item, List

class HomePageTest(TestCase):

	def test_home_page_contains_todo_list(self):
		request = HttpRequest()
		response = home_page(request)
		expected_content = render_to_string('home.html',request=request)
		#use decode to compare byte with string
		self.assertEqual(response.content.decode(), expected_content)
		
class NewListViewTest(TestCase):

	def test_can_save_post_requests_to_db(self):
		response = self.client.post('/lists/new', {'item_text': 'New item'})
		
		item_from_db = Item.objects.all()[0]
		self.assertEqual(item_from_db.text, 'New item')	
		
	def test_redirects_to_list_url(self):
		response = self.client.post('/lists/new', {'item_text': 'New item'})
		self.assertEqual(response.status_code, 302)
		new_list = List.objects.first()
		self.assertRedirects(response, '/lists/%d/' % (new_list.id))


class ListViewTest(TestCase):

	def test_lists_page_shows_items_from_db(self):
		our_list = List.objects.create()
		Item.objects.create(text='Item 1',list=our_list)
		Item.objects.create(text='Item 2',list=our_list)
		other_list = List.objects.create()
		Item.objects.create(text='Bad Item',list=other_list)
		
		response = self.client.get('/lists/%d/' % (our_list.id))

		self.assertContains(response, 'Item 1')
		self.assertContains(response, 'Item 2')
		self.assertNotContains(response, 'Bad Item')

	def test_uses_lists_template(self):
		our_list = List.objects.create()
		response = self.client.get('/lists/%d/' % (our_list.id))

		self.assertTemplateUsed(response, 'lists.html')

	def test_passes_list_to_template(self):
		our_list = List.objects.create()
		response = self.client.get('/lists/%d/' % (our_list.id))
		#.context is a Django test method
		self.assertEqual(response.context['list'],our_list)

class AddItemToExistingList(TestCase):
	
	def test_add_item_to_existing_list(self):
		our_list = List.objects.create()
		self.client.post('/lists/%d/add' % (our_list.id),
			{'item_text': 'new item to existing list'})
		
		new_item = Item.objects.first()
		self.assertEqual(new_item.list, our_list)
		self.assertEqual(new_item.text,'new item to existing list')
	
	def test_redirect_to_list_page(self):
		other_list = List.objects.create()
		our_list = List.objects.create()
		response = self.client.post('/lists/%d/add' % (our_list.id,),
			{'item_text': 'new item to existing list'})
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/lists/%d/' % (our_list.id))
		
class ItemModelTest(TestCase):

	def test_saving_and_retrieving_from_db(self):
		first_list = List()
		first_list.save()

		first_item = Item()
		first_item.text = 'Very first item'
		first_item.list = first_list
		first_item.save() 
		
		second_item = Item()
		second_item.text = 'The second item'
		second_item.list = first_list
		second_item.save()

		first_item_from_db = Item.objects.all()[0]
		self.assertEqual(first_item_from_db.text, 'Very first item')
		self.assertEqual(first_item_from_db.list, first_list)

		second_item_from_db = Item.objects.all()[1]
		self.assertEqual(second_item_from_db.text, 'The second item')
		self.assertEqual(second_item_from_db.list, first_list)
 
