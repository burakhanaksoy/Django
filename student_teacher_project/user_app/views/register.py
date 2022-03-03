from django.contrib.auth.models import User
from rest_framework import generics
from user_app.api.serializers import RegisterSerializer
from rest_framework import status
from rest_framework.response import Response


class RegisterUser(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        data = {}
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            data = serializer.save()
        else:
            data['errors'] = serializer.errors

        if 'errors' in data.keys():
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_201_CREATED)
