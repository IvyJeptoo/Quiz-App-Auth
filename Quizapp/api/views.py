from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .permissions import IsStudentUser, IsTeacherUser
from django.shortcuts import render, get_object_or_404
from ..models import Profile
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view


class TeacherSignupView(generics.GenericAPIView):
    serializer_class=TeacherSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message": "account created successfully"
        })

class StudentSignupView(generics.GenericAPIView):
    serializer_class=StudentSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message": "account created successfully"
        })

class CustomAuthToken(ObtainAuthToken):
    def post(self,request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created= Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id':user.pk,
            'is_student':user.is_student,
            'username':user.username

        })

class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class StudentOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsStudentUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class TeacherOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsTeacherUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

# class ProfileView(APIView):
#     def get(self, request,*args*kwargs):
#         user = request.user
#         profile = get_object_or_404(get_user_model(), username=user.username).profile
#         serializer = ProfileSerializer(profile)

#         return Response(serializer.data)

# class CategoryListView(APIView):
#     def get(self, request):
#         categories = Category.objects.all
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsTeacherUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)





