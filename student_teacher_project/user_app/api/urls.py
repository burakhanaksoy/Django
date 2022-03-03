from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.views.register import RegisterUser as register
from user_app.views.logout import Logout as logout

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', register.as_view(), name='register'),
    path('logout/', logout.as_view(), name='logout'),
]
