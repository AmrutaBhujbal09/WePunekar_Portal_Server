from rest_framework import serializers
from .models import Luggage
#here BLOG IS MODEL NAME


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Luggage

        fields = ["id","address","aadhar_card","duration","luggage_info","user_id","wearhouse"]
