from django.conf.urls import url
from .views import (CreateRequesttAPIView,GetRequestDetailsAPIView,RequestListView)

urlpatterns = [
    url('request',CreateRequesttAPIView.as_view()),
    url('details/(?P<pk>.+)',GetRequestDetailsAPIView.as_view()),
    url('getRequestList',RequestListView.as_view())
]