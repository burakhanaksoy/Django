from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication

class Logout(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = []
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        data = {"msg":"logout successfully."}
        return Response(data, status= status.HTTP_200_OK)
