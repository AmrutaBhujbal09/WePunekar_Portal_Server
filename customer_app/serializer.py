from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email","password","username","contact_number","type_c"]


    def create(self,validated_data):
        user=User.objects.create_user(
            first_name=validated_data.pop('first_name'),
            last_name=validated_data.pop('last_name'),
            username=validated_data.pop('username'),
            email=validated_data.pop('email'),
            password=validated_data.pop('password'),
          #  address=validated_data.pop('address'),
           # aadhar_card=validated_data.pop('aadhar_card'),
            contact_number=validated_data.pop('contact_number'),
            type_c=validated_data.pop('type_c')
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    email=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
    type_user=serializers.CharField(required=True)

    def validate(self,attrs):
        self.user=authenticate(username=attrs.pop("email"),password=attrs.pop("password"))

        if self.user:
            return attrs
        else:
               raise serializers.ValidationError()

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","first_name","last_name","email","contact_number"]