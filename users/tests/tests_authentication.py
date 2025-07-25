from django.test import TestCase
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.test import Client
from users.tests.util import print_response
import json

class AuthTestCase(TestCase):
	
	fixtures = ["initial_data"]
		
	@classmethod
	def setUpTestData(cls):
		cls.MyUser = get_user_model()
		cls.MyUser.objects.create_user(username='testuser', password='testuser', role='ENTREPRENEUR', phone_no='123')
		cls.client = Client()
	
	def test_multiple_signup(self):
		print("\n---------------/auth/signup/---------------\n")
		response = self.client.post(
		    "/auth/signup/",
		    data=json.dumps({
			"username": "avico",
			"password": "sex123",
			"role": "INVESTOR",
		    }),
		    content_type="application/json"
		)
		print_response(response)
		
		print("\n---------------/auth/signup/ again---------------\n")
		response = self.client.post(
		    "/auth/signup/",
		    data=json.dumps({
			"username": "avico",
			"password": "sex1234",
			"role": "ENTREPRENEUR",
		    }),
		    content_type="application/json"
		)
		self.assertEqual(response.text, "User already exists")
	
	def test_signin(self):
		print("\n---------------/auth/signin/---------------\n")
		response = self.client.post(
		    "/auth/signin/",
		    data=json.dumps({
			"username": "testuser",
			"password": "testuser",
		    }),
		    content_type="application/json"
		)
		print_response(response)
	
	def test_invalid_signin(self):
		print("\n---------------/auth/signin/ invalid---------------\n")
		response = self.client.post(
		    "/auth/signin/",
		    data=json.dumps({
			"username": "testuser",
			"password": "testuserw",
		    }),
		    content_type="application/json"
		)
		self.assertEqual(response.text, "Invalid username password")
