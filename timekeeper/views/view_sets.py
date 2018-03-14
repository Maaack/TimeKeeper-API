from .serializers import *
from timekeeperapi.mixins.view_sets import BaseViewSet


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


class PositionViewSet(BaseViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class NoteViewSet(BaseViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
