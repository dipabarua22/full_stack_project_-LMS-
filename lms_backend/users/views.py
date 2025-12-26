from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from users.models import User
from . serializers import UserSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def user_list_create(request):
    if not request.user.is_authenticated:
            return Response({'detail' : 'Authentication Credentials is not provided'},status=401)

    if request.method == 'GET':
        if request.user.role == 'admin':
            users = User.objects.all()

        else:
            users = User.objects.filter(id=request.user.id)

        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.user.role == 'admin':

            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors,status =400)
        else:
              return Response({'detail' : 'you have no access'},status=401)