from rest_framework import serializers
from . import (Timeline,
               TimeKeeper)


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
                  'axis')


class TimeKeeperSerializer(BaseModelSerializer):
    class Meta:
        model = TimeKeeper
        fields = ('id', 'created', 'updated', 'user',
                  'timeline')