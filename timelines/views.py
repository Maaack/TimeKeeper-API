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


class ActionViewSet(BaseViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class ActivityViewSet(BaseViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class PerspectiveViewSet(BaseViewSet):
    queryset = Perspective.objects.all()
    serializer_class = PerspectiveSerializer


class ElementViewSet(BaseViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class ActorViewSet(BaseViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class SetViewSet(BaseViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer


class RelativePositionViewSet(BaseViewSet):
    queryset = RelativePosition.objects.all()
    serializer_class = RelativePositionSerializer


class AliasViewSet(BaseViewSet):
    queryset = Alias.objects.all()
    serializer_class = AliasPositionSerializer


