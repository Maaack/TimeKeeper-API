from rest_framework import serializers
from timekeeper.models import *

FIELDS_LIST_ID = ('id', )
FIELDS_LIST_TIMESTAMPED_OWNABLE = ('created', 'updated', 'user')
FIELDS_LIST_COMMON_OBJECT = FIELDS_LIST_ID + FIELDS_LIST_TIMESTAMPED_OWNABLE
FIELDS_LIST_GENERIC_OPERATION = FIELDS_LIST_COMMON_OBJECT + ('started', 'ended', 'running', 'milliseconds')
FIELDS_LIST_RAW_TITLE = ('raw_title', 'title')
FIELDS_LIST_COMMON_OBJECT_TITLE = FIELDS_LIST_COMMON_OBJECT + ('raw_title', 'title')
FIELDS_LIST_RAW_TEXT = ('raw_text', 'text')
FIELDS_LIST_COMMON_OBJECT_TEXT = FIELDS_LIST_COMMON_OBJECT + ('raw_text', 'text')


class ReadOnlyUserMixinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        abstract = True
        fields = FIELDS_LIST_COMMON_OBJECT

    user = serializers.ReadOnlyField(source='user.username')


class AxisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Axis
        fields = FIELDS_LIST_COMMON_OBJECT + ('maximum_position', 'minimum_position')


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = FIELDS_LIST_COMMON_OBJECT_TITLE + ('axis', 'value')


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = FIELDS_LIST_COMMON_OBJECT_TEXT + ('positions', 'snippet')


class TimelineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timeline
        fields =  FIELDS_LIST_COMMON_OBJECT_TEXT + ('axis', )


class TimeKeeperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeKeeper
        fields = FIELDS_LIST_COMMON_OBJECT + ('timeline', )

