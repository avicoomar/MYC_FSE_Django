from django.http import HttpResponseForbidden

#This is a custom @login_required decorator that works just like @login_required, except that it sends 403 status code, not 302
def login_required_403(view_func):
	def _wrapped_view(request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden("Forbidden")
		return view_func(request, *args, **kwargs)
	return _wrapped_view
