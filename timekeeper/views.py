from django.shortcuts import render

# Create your views here.
from .models.serializers import *

from rest_framework.response import Response
from rest_framework.decorators import detail_route
from timekeeperapi.mixins.views import BaseViewSet


# Create your views here.
class TimelineViewSet(BaseViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer


class TimeKeeperViewSet(BaseViewSet):
    queryset = TimeKeeper.objects.all()
    serializer_class = TimeKeeperSerializer


class AxisViewSet(BaseViewSet):
    queryset = Axis.objects.all()
    serializer_class = AxisSerializer
