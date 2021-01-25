from django.db import models
from customer_app.models import User
class Luggage(models.Model):

    Godown_Choice=(
        ('BALEWADI','Balewadi'),
        ('SHIVAJINAGAR','Shivajinagar')
    )


    address = models.CharField(max_length=60, blank=False, null=False)
    #pincode = models.TextField(max_length=6 ,blank=False, null=False,default=411027)
    aadhar_card = models.IntegerField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    luggage_info = models.TextField(max_length=60 ,blank=False, null= False)
    wearhouse = models.CharField(max_length=15 ,blank=False, null=False,choices=Godown_Choice,default='BALEWADI')
    user_id = models.ForeignKey(User, null=False, blank=False , on_delete=models.CASCADE)

