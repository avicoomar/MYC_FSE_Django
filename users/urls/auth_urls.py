from django.urls import path
from users.views import auth_views

urlpatterns = [
    path("signup/", auth_views.signup, name="signup"),
    path("signin/", auth_views.signin, name="signin"),
    path("refresh-token/", auth_views.refresh_token, name="refresh-token"),
    path("signout/", auth_views.signout, name="signout"),
]
