from django.shortcuts import render
from django.http import JsonResponse
from api.models import User
from django.shortcuts import get_object_or_404

from api.serializer import UserSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import User, Services, UsedList
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializer import CustomTokenObtainPairSerializer
from api.serializer import ServicesSerializer, UsedListSerializer






class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer





class UserListCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        # Get all users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Create a new user
        serializer = UserSerializer(data=request.data)
    def post(self, request):
        # data = request.data.copy()
        # data['parent'] = request.user.parent.id
        newUser = request.data
        serializer = UserSerializer(data=newUser)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserDetailAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        # Get user by primary key (id)
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        # Update the user details
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=False)  # Use partial=False for full update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        # Update the user with partial data (for example, just changing the username)
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)  # Use partial=True for partial update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        # Delete the user
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    




class ServicesCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        users = Services.objects.all()
        serializer = ServicesSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServicesDetailAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        services = get_object_or_404(User, pk=pk)
        serializer = ServicesSerializer(services)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        services = get_object_or_404(User, pk=pk)
        serializer = ServicesSerializer(services, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        services = get_object_or_404(User, pk=pk)
        services.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class usedlistCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        usedlist = UsedList.objects.all()
        serializer = UsedListSerializer(usedlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UsedListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class usedlistDetailAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        usedlist = get_object_or_404(UsedList, pk=pk)
        serializer = UsedListSerializer(usedlist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        usedlist = get_object_or_404(UsedList, pk=pk)
        serializer = ServicesSerializer(usedlist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        usedlist = get_object_or_404(UsedList, pk=pk)
        usedlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
