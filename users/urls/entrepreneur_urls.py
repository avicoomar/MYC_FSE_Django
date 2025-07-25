from django.urls import path
from users.views import entrepreneur_views

urlpatterns = [
	path("testEntrepreneur/", entrepreneur_views.test_entrepreneur, name="test_entrepreneur"),
	path("investors/", entrepreneur_views.get_investors, name="get_investors"),
	path("companies/", entrepreneur_views.get_own_companies, name="get_own_companies"),
	path("add_entrepreneur/", entrepreneur_views.add_entrepreneurdetail, name="add_entrepreneurdetail"),
]
