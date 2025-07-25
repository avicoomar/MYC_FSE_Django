import json

def print_response(response):
	print("====== Response ======")
	print(f"Response headers:\n {json.dumps(dict(response.items()), indent=2)}")
	print(f"Response cookies: {response.cookies}")
	print(f"Response status code: {response.status_code}")
	print(f"Response data: {response.text}")
