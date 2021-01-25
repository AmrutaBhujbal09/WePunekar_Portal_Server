from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    Status_Choice = (
        ('USER', 'User'),
        ('STAFF', 'Staff')
    )

    email = models.EmailField('email_address', unique=True)
    contact_number = models.TextField(max_length=10, null=True, blank=False)
    #address = models.TextField(max_length=60, null=True, blank=False)
   # aadhar_card=models.BigIntegerField()
    type_c= models.CharField(max_length=10, null=False, blank=False, choices=Status_Choice, default='USER')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
