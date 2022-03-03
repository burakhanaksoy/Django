from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person
from .serializers import PersonSerializer
# Create your views here.


@api_view(['POST'])
def create_user(request):

    print(request)

    serializer = PersonSerializer(data=request.data)


    if not serializer.is_valid():
        return Response(data=None, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data

    Person.objects.create(**data)

    return Response(status=status.HTTP_201_CREATED)
