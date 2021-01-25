from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import User
from rest_framework import status
from .serializer import (UserSignupSerializer, UserLoginSerializer)
from rest_framework.generics import (GenericAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView)
from rest_framework.response import Response

# Create your views here.

class UserSignupAPIView(CreateAPIView):
    serializer_class=UserSignupSerializer

    def post(self,request,*args,**kwargs):
        print("requested data:",request.data)
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            obj=User.objects.get(email=request.data["email"])

            response_data={
                "id":obj.id,
                "first_name":obj.first_name,
                "last_name":obj.last_name,
                "emai":obj.email
            }

            return Response(response_data,status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(GenericAPIView):

    serializer_class=UserLoginSerializer
    def post(self,request,*args,**kwargs):
        print("requested data:", request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            obj=serializer.user

            if request.data["type_user"]==obj.type_c:
                response_data={
                    "id":obj.id,
                    "first_name":obj.first_name,
                    "last_name":obj.last_name,
                    "email":obj.email,
                    "type":obj.type_c
                }

                return Response(response_data,status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class DeleteUserAPIView(DestroyAPIView):
    def delete(self,request,*args,**kwargs):
        user_id=self.kwargs["pk"]
        User.objects.filter(id=user_id).delete()
        return Response(status.HTTP_204_NO_CONTENT)