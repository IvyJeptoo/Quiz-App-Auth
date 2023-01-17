from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from rest_framework.authtoken.models import Token


class TeacherSignupView(generics.GenericAPIView):
    serializer_class=TeacherSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=user.get_serializer_context()).data,
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
            "user":UserSerializer(user, context=user.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message": "account created successfully"
        })