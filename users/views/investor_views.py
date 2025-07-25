from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from users.util import login_required_403


@login_required_403
def test_investor(request):
	return HttpResponse("Test Investor", content_type="text/plain", status=200)

@login_required_403
@permission_required(["users.view_company"], raise_exception=True)
def get_companies(request):
	#TODO: List Companies that investors can invest in & their POCs - Entrepreneurs
	return HttpResponse("ALl the listed companies at MYC", content_type="text/plain", status=200)
