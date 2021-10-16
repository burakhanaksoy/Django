from django.contrib.auth.models import User
from rest_framework import generics
from user_app.api.serializers import RegisterSerializer


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []
    authentication_classes = []
