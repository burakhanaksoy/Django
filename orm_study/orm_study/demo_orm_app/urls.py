
from django.urls import path
from .views import *

urlpatterns = [
    path('user/create/', create_user)
]
