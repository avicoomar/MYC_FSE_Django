import jwt
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse

#Validates & attaches jwt to the request like <request.jwt> if jwt is valid - kinda similar to what SessionMiddleware does i.e. request.session
class JWTAttachMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
	
	def __call__(self, request):
		
		#no point of attaching jwt to request for /admin therefore /admin requests are allowed directly
		if(request.path.startswith("/admin")):
			response = self.get_response(request)
			return response	
			
		jwt_token_received = request.headers.get("Authorization")
		try:
			jwt_token = jwt.decode(jwt_token_received, "coomar", algorithms=["HS256"])
			request.jwt = jwt_token
			response = self.get_response(request)
		except Exception as e:
			#Do not attach jwt to request i.e. no request.jwt
			response = self.get_response(request)
		
		return response

#Attaches user to request like <request.user> - kinda similar to what AuthenticationMiddleware does
#This middleware is tightly coupled to JWTAttachMiddleware as it relies on request.jwt for fetching user
class UserAttachMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
	
	def __call__(self, request):
		
		#/admin relies on request.user & it shall not be affected by this middleware therefore /admin requests are allowed directly
		if(request.path.startswith("/admin")):
			response = self.get_response(request)
			return response	
		
		MyUser = get_user_model()
			
		if "jwt" in dir(request):
			user = MyUser.objects.get(id=request.jwt.get("userid"))
			request.user = user
			response = self.get_response(request)
			return response
		
		request.user = AnonymousUser()
		response = self.get_response(request)
		
		return response
	
#This middleware is used only for development purpose!
class CorsMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
	
	def __call__(self, request):
		
		#Handle preflight (OPTIONS) request
		if request.method == "OPTIONS":
			response = HttpResponse(status=200) #Don't continue the middleware chain
		else:
			response = self.get_response(request) #Continue the middleware chain	
		
		response["Access-Control-Allow-Origin"] = "http://localhost:3000"
		response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
		response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
		response["Access-Control-Allow-Credentials"] = "true"
		
		return response
