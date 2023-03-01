from rest_framework import serializers
from Quizapp.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['username', 'email', 'is_student']


class TeacherSignupSerializer(serializers.ModelSerializer):
    confirmPassword=serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    class Meta:
        model=User
        fields=["username","email","password","confirmPassword"]
        extra_kwargs={
            'password':{'write_only': True}
        }

    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        confirmPassword=self.validated_data['confirmPassword']
        if password != confirmPassword:
            raise serializers.ValidationError({"error": "passwords do not match"})

        user.set_password(password)
        user.is_teacher=True
        user.save()
        Teacher.objects.create(user=user)
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ['bio', 'avatar']


class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = '__all__'

class StudentSignupSerializer(serializers.ModelSerializer):
    confirmPassword=serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    class Meta:
        model=User
        fields=["username","email","password","confirmPassword"]
        extra_kwargs={
            'password':{'write_only': True}
        }

    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        confirmPassword=self.validated_data['confirmPassword']
        if password != confirmPassword:
            raise serializers.ValidationError({"error": "passwords do not match"})

        user.set_password(password)
        user.is_student=True
        user.save()
        Student.objects.create(user=user)
        return user
    

    