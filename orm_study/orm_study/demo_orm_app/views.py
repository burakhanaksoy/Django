from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Company, Person
from .serializers import PersonSerializer, CompanySerializer
# Create your views here.


@api_view(['POST'])
def user_create(request):
    serializer = PersonSerializer(data=request.data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response(data=None, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    serializer.save()

    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def company_create(request):
    serializer = CompanySerializer(data=request.data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response(data=None, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data

    Company.objects.create(**data)

    return Response(status=status.HTTP_201_CREATED)