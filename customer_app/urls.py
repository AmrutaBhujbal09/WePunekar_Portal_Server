from django.conf.urls import url
from.views import (UserSignupAPIView,UserLoginAPIView,DeleteUserAPIView)
urlpatterns=[
    url('signup',UserSignupAPIView.as_view()),
    url('login',UserLoginAPIView.as_view()),
    url('delte/(?P<pk>.+)',DeleteUserAPIView.as_view())
]
