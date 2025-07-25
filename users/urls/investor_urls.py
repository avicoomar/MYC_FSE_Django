from django.urls import path
from users.views import investor_views

urlpatterns = [
	path("testInvestor/", investor_views.test_investor, name="test_investor"),
	path("companies/", investor_views.get_companies, name="get_companies"),
]
