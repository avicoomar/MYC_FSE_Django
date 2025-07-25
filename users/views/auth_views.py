from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import Group
import json
import uuid
import jwt
import time, datetime
from datetime import datetime, timedelta, timezone

MyUser = get_user_model()

def signup(request):
	
	request_body = json.loads(request.body)
	
	if MyUser.objects.filter(username = request_body.get("username")).exists():
		return HttpResponse("User already exists", content_type="text/plain")
	
	refresh_token = str(uuid.uuid4()) #generate refresh_token
	user = MyUser.objects.create_user(first_name=request_body.get("firstName", ""), \
									last_name=request_body.get("lastName", ""), \
									username=request_body.get("username"), \
									password=request_body.get("password"), \
									role=request_body.get("role"), \
									phone_no=request_body.get("phoneNo", ""), \
									refresh_token=refresh_token)
	if user.role == "INVESTOR":
		user.groups.set([Group.objects.get(name="investor_group")])
	if user.role == "ENTREPRENEUR":
		user.groups.set([Group.objects.get(name="entrepreneur_group")])
	user.save() #Save user along with his refresh token & permission_group in db
	jwt_token = jwt.encode({\
					"userid": user.id, \
					"role": user.role, \
					"exp": datetime.now(timezone.utc) + timedelta(minutes=3), \
				}, "coomar", algorithm="HS256") #generate jwt_token
	response = HttpResponse(jwt_token, content_type="text/plain", status=200) #set jwt_token as response body
	response.set_cookie("refresh_token", value=refresh_token, path="/", httponly=True) #set refresh_token as response cookie
	return response

def signin(request):
	
	request_body = json.loads(request.body)
	
	user = authenticate(username=request_body.get("username"), password=request_body.get("password"))
	
	if user != None:
		jwt_token = jwt.encode({\
						"userid": user.id, \
						"role": user.role, \
						"exp": datetime.now(timezone.utc) + timedelta(minutes=3), \
					}, "coomar", algorithm="HS256") #generate jwt_token
		response = HttpResponse(jwt_token, content_type="text/plain", status=200) #set jwt_token as response body
		response.set_cookie("refresh_token", value=user.refresh_token, path="/", httponly=True) #set user's existing refresh_token as response cookie
		return response
	
	return HttpResponse("Invalid username password", content_type="text/plain", status=200)

#API for browser(frontend) to refresh jwt token (that expired after 3 mins), since the frontend cannot always call /signin to get new JWT Token
def refresh_token(request):
	
	refresh_token_received = request.COOKIES.get("refresh_token")
	
	#Find user by refresh_token received in request (chances of finding multiple users are astronomically low)
	user_fetched = MyUser.objects.filter(refresh_token=refresh_token_received).first()
	
	#if user found then user valid, so return new jwt token
	if user_fetched:
		jwt_token = jwt.encode({\
						"userid": user_fetched.id, \
						"role": user_fetched.role, \
						"exp": datetime.now(timezone.utc) + timedelta(minutes=3), \
					}, "coomar", algorithm="HS256")
		
		return HttpResponse(jwt_token, content_type="text/plain", status=200)
	
	return HttpResponse("JWT token cannot be refreshed", content_type="text/plain", status=200)

#API for browser(frontend) to clear it's refresh_token cookie
def signout(request):
	response = HttpResponse()
	response.delete_cookie("refresh_token", path="/")
	return response
