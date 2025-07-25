from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Roles(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    INVESTOR = "INVESTOR", "Investor"
    ENTREPRENEUR = "ENTREPRENEUR", "Entrepreneur"
    

class MyUser(AbstractUser):
	role = models.CharField(max_length=35, choices=Roles.choices)
	phone_no = models.CharField(max_length=15) #Type is CharField to avoid issues with formatting, country codes, etc.
	refresh_token = models.CharField(blank=True, max_length=200)

class InvestorDetail(models.Model):
	#id = models.AutoField(primary_key=True) --> created automatically by Django
	user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
	class Meta:
		permissions = [
			("view_own_investordetail", "Can view own investordetails"),
			("change_own_investordetail", "Can change own investordetails"),
			("delete_own_investordetail", "Can delete own investordetails"),
		]
	
class EntrepreneurDetail(models.Model):
	#id = models.AutoField(primary_key=True) --> created automatically by Django
	user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
	class Meta:
		permissions = [
			("view_own_entrepreneurdetail", "Can view own entrepreneurdetails"),
			("change_own_entrepreneurdetail", "Can change own entrepreneurdetails"),
			("delete_own_entrepreneurdetail", "Can delete own entrepreneurdetails"),
		]

class Company(models.Model):
	#id = models.AutoField(primary_key=True) --> created automatically by Django
	entrepreneur = models.ForeignKey(EntrepreneurDetail , on_delete=models.CASCADE)
	class Meta:
		permissions = [
			("view_own_company", "Can view own companies"),
			("change_own_company", "Can change own companies"),
			("delete_own_company", "Can delete own companies"),
		]
