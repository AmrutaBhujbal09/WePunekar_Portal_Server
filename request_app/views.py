from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import (DestroyAPIView,GenericAPIView,CreateAPIView,UpdateAPIView,ListAPIView)

from rest_framework.response import Response
from customer_app.models import User
from .serializer import (RequestSerializer)

from .models import Luggage

class CreateRequesttAPIView(CreateAPIView):
    serializer_class = RequestSerializer

    def post(self, request, *args, **kwargs):
        print("request data",request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class GetRequestDetailsAPIView(ListAPIView):
    serializer_class = RequestSerializer

    def get(self, request, *args, **kwargs):
        data =list()
        req_id = self.kwargs["pk"]
        req_data = Luggage.objects.filter(id=req_id)
        serializer = self.get_serializer(req_data,many=True)

        for request_app in serializer.data:
            get_user = User.objects.filter(id=request_app["user_id"]).values("first_name", "last_name", "contact_number","type_c","email")

            data.append({
                "id": request_app["id"],
                "Address": request_app["address"],
                "wearhouse":request_app["wearhouse"],
                "Aadhar Card No": request_app["aadhar_card"],
                "Duration": request_app["duration"],
                "Luggage Description": request_app["luggage_info"],
                "user_id": request_app["user_id"],
                "first_name": get_user[0]["first_name"],
                "last_name": get_user[0]["last_name"],
                "email": get_user[0]["email"],
                "User Type": get_user[0]["type_c"],
                "Contact No": get_user[0]["contact_number"],
                #Wearhouse":get_user[0]["wearhouse"]

            })

            return Response(data, status.HTTP_200_OK)


class RequestListView(ListAPIView):
    serializer_class=RequestSerializer

    def get_queryset(self):
        get_choice =self.request.data["wearhouse"]
        rdata= Luggage.objects.filter(wearhouse=get_choice)
        return rdata

    def post(self, request , *args ,**kwargs):
        data=list()
        get_choice = request.data["wearhouse"]
        rdata = Luggage.objects.filter(wearhouse=get_choice)
        serializer = self.get_serializer(rdata,many=True)

        for request_app in serializer.data:
            get_user = User.objects.filter(id=request_app["user_id"]).values("first_name", "last_name", "contact_number","type_c","email")

            data.append({
                "id": request_app["id"],
                "Address": request_app["address"],
                "wearhouse":request_app["wearhouse"],
                "Aadhar Card No": request_app["aadhar_card"],
                "Duration": request_app["duration"],
                "Luggage Description": request_app["luggage_info"],
                "user_id": request_app["user_id"],
                "first_name": get_user[0]["first_name"],
                "last_name": get_user[0]["last_name"],
                "email": get_user[0]["email"],
                "User Type": get_user[0]["type_c"],
                "Contact No": get_user[0]["contact_number"],
                #Wearhouse":get_user[0]["wearhouse"]

            })

            return Response(data, status.HTTP_200_OK)


