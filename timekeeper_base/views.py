from django.shortcuts import render

# Create your views here.
from .models.serializers import *

from rest_framework.response import Response
from rest_framework.decorators import detail_route
from api.mixins.views import BaseViewSet


# Create your views here.
class TimelineViewSet(BaseViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer


class TimeViewSet(BaseViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class TimeLinkViewSet(BaseViewSet):
    queryset = TimeLink.objects.all()
    serializer_class = TimeLinkSerializer


class TimeKeeperViewSet(BaseViewSet):
    queryset = TimeKeeper.objects.all()
    serializer_class = TimeKeeperSerializer


class EventViewSet(BaseViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer