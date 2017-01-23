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
               Set,
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
                  'times', 'time_links')

    times = serializers.HyperlinkedRelatedField(many=True, view_name='time-detail', read_only=True)


class TimeSerializer(BaseModelSerializer):
    class Meta:
        model = Time
        fields = ('id', 'created', 'updated', 'user',
                  'interval_type', 'interval_duration', 'timelines', 'time_links', 'events')


class TimeLinkSerializer(BaseModelSerializer):
    class Meta:
        model = TimeLink
        fields = ('id', 'created', 'updated', 'user',
                  'order', 'timeline', 'time')


class TimeKeeperSerializer(BaseModelSerializer):
    class Meta:
        model = TimeKeeper
        fields = ('id', 'created', 'updated', 'user',
                  'timeline')


class EventSerializer(BaseModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'created', 'updated', 'user', 'raw_text', 'text',
                  'event_rule', 'time', 'place', 'action')


class ActionSerializer(BaseModelSerializer):
    class Meta:
        model = Action
        fields = ('id', 'created', 'updated', 'user',
                  'actors', 'activity')


class ActivitySerializer(BaseModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'created', 'updated', 'user', 'raw_text', 'text')


class PerspectiveSerializer(TimeKeeperSerializer):
    class Meta:
        model = Perspective
        fields = ('id', 'created', 'updated', 'user', 'raw_title', 'title',
                  'timeline')


class ElementSerializer(PerspectiveSerializer):
    class Meta:
        model = Element
        fields = ('id', 'created', 'updated', 'user', 'raw_title', 'title',
                  'aliases', 'timeline')

    aliases = serializers.HyperlinkedRelatedField(many=True, view_name='alias-detail', read_only=True)


class ActorSerializer(ElementSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'created', 'updated', 'user', 'raw_title', 'title',
                  'type', 'aliases', 'timeline')


class SetSerializer(ElementSerializer):
    class Meta:
        model = Set
        fields = ('id', 'created', 'updated', 'user', 'raw_title', 'title',
                  'type', 'method', 'actors', 'aliases', 'timeline')


class RelativePositionSerializer(BaseModelSerializer):
    class Meta:
        model = RelativePosition
        fields = ('id', 'created', 'updated', 'user', 'raw_title', 'title',
                  'type', 'method', 'actors', 'aliases')


class AliasPositionSerializer(BaseModelSerializer):
    class Meta:
        model = Alias
        fields = ('id', 'created', 'updated', 'user', 'raw_title', 'title',
                  'element', 'type')
