from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

	def test_home_page_contains_todo_list(self):
		request = HttpRequest()

		response = home_page(request)
		
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>To-Do Lists</title>', response.content)
		self.assertTrue(response.content.strip().endswith(b'</html>'))
		
		with open('lists/templates/home.html') as f:
			expected_content=f.read()
		
		#use decode to compare byte with string
		self.assertEqual(response.content.decode(), expected_content)
		
