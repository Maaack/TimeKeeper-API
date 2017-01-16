from rest_framework import serializers
from . import (Timeline,
               Time,
               TimeLink,
               TimeKeeper,
               EventRule,
               Event,
               Action,
               Activity,
               Perspective,
               Element,
               Actor,
               Product,
               RelativePosition,
               Alias)


class BaseModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        abstract = True
        fields = ('id', 'created', 'updated', 'user')

    user = serializers.ReadOnlyField(source='user.username')


class RawTitleSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ('id', 'raw_title', 'title')


class RawTextSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ('id', 'raw_text', 'text')


class TimelineSerializer(BaseModelSerializer, RawTitleSerializer):
    class Meta:
        model = Timeline
        fields = ('id', 'created', 'updated', 'user', 'raw_title', 'title',
                  'times')

    times = serializers.HyperlinkedRelatedField(many=True, view_name='time-detail', read_only=True)


class TimeSerializer(BaseModelSerializer):
    class Meta:
        model = Time
        fields = ('id', 'created', 'updated', 'user',
                  'interval_type', 'interval_duration')


class TimeLinkSerializer(BaseModelSerializer):
    class Meta:
        model = TimeLink
        fields = ('id', 'created', 'updated', 'user',
                  'order', 'timeline', 'time')

    time = serializers.HyperlinkedRelatedField(view_name='time-detail', read_only=True)
    timeline = serializers.HyperlinkedRelatedField(view_name='timeline-detail', read_only=True)


class TimeKeeperSerializer(BaseModelSerializer):
    class Meta:
        model = TimeKeeper
        fields = ('id', 'created', 'updated', 'user',
                  'timeline')

    timeline = serializers.HyperlinkedRelatedField(view_name='timeline-detail', read_only=True)


