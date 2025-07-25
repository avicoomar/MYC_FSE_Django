from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("users.urls.auth_urls")),
    path("investor/", include("users.urls.investor_urls")),
    path("entrepreneur/", include("users.urls.entrepreneur_urls")),
]
