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
		
