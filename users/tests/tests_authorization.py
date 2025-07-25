from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import Client
from users.tests.util import print_response
import json

class EntrepreneurTests(TestCase):
	
	fixtures = ["initial_data"]
	
	@classmethod
	def setUpTestData(cls):
		cls.MyUser = get_user_model()
		cls.client = Client()
		response = cls.client.post("/auth/signup/", data=json.dumps({
			"username" : "testentrepreneur",
			"password" : "testentrepreneur",
			"role": "ENTREPRENEUR",
		}), content_type="application/json")
		cls.jwt_token_ent = response.text
		response = cls.client.post("/auth/signup/", data=json.dumps({
			"username" : "testinvestor",
			"password" : "testinvestor",
			"role": "INVESTOR",
		}), content_type="application/json")
		cls.jwt_token_inv = response.text

	
	def test_entrepreneur(self):
		print("\n---------------/entrepreneur/testEntrepreneur/---------------\n")
		response = self.client.get("/entrepreneur/testEntrepreneur/", HTTP_Authorization = self.jwt_token_ent)
		self.assertEqual(response.text, "Test Entrepreneur")
	
	def test_invalid_entrepreneur(self):
		print("\n---------------/entrepreneur/testEntrepreneur/ invalid jwt---------------\n")
		response = self.client.get("/entrepreneur/testEntrepreneur/", HTTP_Authorization = self.jwt_token_ent + "xyz") #tampered jwt
		self.assertEqual(response.status_code, 403)
		print("\n---------------/entrepreneur/testEntrepreneur/ no jwt---------------\n")
		response = self.client.get("/entrepreneur/testEntrepreneur/") #no jwt
		self.assertEqual(response.status_code, 403)
	
	def test_investor(self):
		print("\n---------------/investor/testInvestor/---------------\n")
		response = self.client.get("/investor/testInvestor/", HTTP_Authorization = self.jwt_token_inv)
		self.assertEqual(response.text, "Test Investor")
	
	def test_invalid_investor(self):
		print("\n---------------/investor/testInvestor/ invalid jwt---------------\n")
		response = self.client.get("/investor/testInvestor/", HTTP_Authorization = self.jwt_token_inv + "xyz") #tampered jwt
		self.assertEqual(response.status_code, 403)
		print("\n---------------/investor/testInvestor/ no jwt---------------\n")
		response = self.client.get("/investor/testInvestor/") #no jwt
		self.assertEqual(response.status_code, 403)
	
	def test_entrepreneur_investors(self):
		print("\n---------------/entrepreneur/investors/---------------\n")
		response = self.client.get("/entrepreneur/investors/", HTTP_Authorization = self.jwt_token_ent) #when entrepreneur tries accessing this api
		self.assertEqual(response.text, "All the investors registered at MYC that wanna invest")
		response = self.client.get("/entrepreneur/investors/", HTTP_Authorization = self.jwt_token_inv) #when investor tries accessing this api
		self.assertEqual(response.status_code, 403)
	
	def test_entrepreneur_companies(self):
		print("\n---------------/entrepreneur/companies/---------------\n")
		response = self.client.get("/entrepreneur/companies/", HTTP_Authorization = self.jwt_token_ent) #when entrepreneur tries accessing this api
		self.assertEqual(response.text, "All the companies owned by the Entrepreneur")
		response = self.client.get("/entrepreneur/companies/", HTTP_Authorization = self.jwt_token_inv) #when investor tries accessing this api
		self.assertEqual(response.status_code, 403)
	
	def test_entrepreneur_add_entrepreneur(self):
		print("\n---------------/entrepreneur/add_entrepreneur/---------------\n")
		response = self.client.get("/entrepreneur/add_entrepreneur/", HTTP_Authorization = self.jwt_token_ent) #when entrepreneur tries accessing this api
		self.assertEqual(response.text, "Entrepreneur details added")
		response = self.client.get("/entrepreneur/add_entrepreneur/", HTTP_Authorization = self.jwt_token_inv) #when investor tries accessing this api
		self.assertEqual(response.status_code, 403)
	
	def test_investor_companies(self):
		print("\n---------------/investor/companies/---------------\n")
		response = self.client.get("/investor/companies/", HTTP_Authorization = self.jwt_token_inv) #when entrepreneur tries accessing this api
		self.assertEqual(response.text, "ALl the listed companies at MYC")
		response = self.client.get("/investor/companies/", HTTP_Authorization = self.jwt_token_ent) #when investor tries accessing this api
		self.assertEqual(response.status_code, 403)
