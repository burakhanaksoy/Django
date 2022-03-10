
from django.urls import path
from .views import *

urlpatterns = [
    path('user/create/', user_create),
    path('company/create/', company_create),
]
