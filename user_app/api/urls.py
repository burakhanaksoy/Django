from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.views.register import RegisterUser as register
from user_app.views.logout import Logout as logout
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', register.as_view(), name='register'),
    path('logout/', logout.as_view(), name='logout'),
    # Use these when use JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
