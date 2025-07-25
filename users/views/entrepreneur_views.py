from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from users.util import login_required_403


@login_required_403
def test_entrepreneur(request):
	return HttpResponse("Test Entrepreneur", content_type="text/plain", status=200)

@login_required_403
@permission_required(["users.view_investordetail"], raise_exception=True)
def get_investors(request):
	#TODO: List Investors & their contact details that are ready to invest in a entrepreneur's company 
	return HttpResponse("All the investors registered at MYC that wanna invest", content_type="text/plain", status=200)

@login_required_403
@permission_required(["users.view_own_company"], raise_exception=True)
def get_own_companies(request):
	#TODO: List the particular entrepreneur's companies
	return HttpResponse("All the companies owned by the Entrepreneur", content_type="text/plain", status=200)

@login_required_403
@permission_required(["users.add_entrepreneurdetail"], raise_exception=True)
def add_entrepreneurdetail(request):
	#TODO: EntrepreneurDetail.objects.create(user=request.user)
	return HttpResponse("Entrepreneur details added", content_type="text/plain", status=200)
