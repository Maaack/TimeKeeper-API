from django.utils.translation import ugettext_lazy as _

from api.mixins.models import *


class BaseModel(TimeStamped, Ownable):
    class Meta:
        abstract = True


class Timeline(BaseModel, RawTitle):
    class Meta:
        verbose_name = _('Timeline')
        verbose_name_plural = _('Timelines')
        ordering = ["-created"]
        default_related_name = 'timelines'

    times = models.ManyToManyField(
        'Time',
        through='TimeLink',
        through_fields=('timeline', 'time'),
    )


class Time(BaseModel):
    class Meta:
        verbose_name = _("Time")
        verbose_name_plural = _("Times")
        ordering = ["-created"]

    interval_type = models.CharField(_("Interval Type"), max_length=20, default="moment")
    interval_duration = models.FloatField(_("Interval Duration"), default=1.0)

    def __str__(self):
        return self.interval_type + " " + str(self.id)


class TimeLink(BaseModel):
    class Meta:
        verbose_name = _("Time Link")
        verbose_name_plural = _("Time Links")
        ordering = ["-created"]
        default_related_name = 'time_links'

    timeline = models.ForeignKey('Timeline')
    time = models.ForeignKey('Time')
    order = models.IntegerField(_("Order"), default=0)

    def __str__(self):
        return self.timeline.title[:25] + ' :: ' + str(self.time)


class TimeKeeper(BaseModel):
    class Meta:
        verbose_name = _("Time Keeper")
        verbose_name_plural = _("Time Keepers")
        ordering = ["-created"]
        default_related_name = 'time_keepers'

    timeline = models.ForeignKey('Timeline', blank=True)

    def save(self, *args, **kwargs):
        try:
            self.timeline
        except Timeline.DoesNotExist:
            self.timeline = Timeline.objects.create()
            if 'raw_title' in kwargs:
                self.timeline.raw_title = kwargs['raw_title'] + ' Timeline'
            self.timeline.save()
        del(kwargs['raw_title'])
        return super(TimeKeeper, self).save(*args, **kwargs)


class EventRule(BaseModel, RawText):
    class Meta:
        verbose_name = _("Event Rule")
        verbose_name_plural = _("Event Rules")
        ordering = ["-created"]
        default_related_name = 'event_rules'

    original_time = models.ForeignKey('Time', null=True)
    repeats = models.BooleanField(_("Repeats"), default=False)
    occurrences = models.IntegerField(_("Occurrences"), default=1)


class Event(BaseModel, RawText):
    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ["-created"]
        default_related_name = 'events'

    event_rule = models.ForeignKey('EventRule', blank=True, null=True)
    perspectives = models.ManyToManyField('Perspective')
    time = models.ForeignKey('Time')
    place = models.ForeignKey('RelativePosition', blank=True, null=True)
    action = models.ForeignKey('Action', blank=True, null=True)


class Action(BaseModel):
    class Meta:
        verbose_name = _("Action")
        verbose_name_plural = _("Actions")
        ordering = ["-created"]
        default_related_name = 'actions'

    actors = models.ManyToManyField('Alias')
    activity = models.ForeignKey('Activity')


class Activity(BaseModel, RawText):
    class Meta:
        verbose_name = _("Activity")
        verbose_name_plural = _("Activities")
        ordering = ["-created"]


class Perspective(TimeKeeper, RawTitle):
    class Meta:
        verbose_name = _("Perspective")
        verbose_name_plural = _("Perspectives")
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        kwargs['raw_title'] = self.raw_title
        return super(Perspective, self).save(*args, **kwargs)


class Element(Perspective):
    class Meta:
        verbose_name = _("Element")
        verbose_name_plural = _("Elements")
        ordering = ["-created"]


class Actor(Element):
    class Meta:
        verbose_name = _("Actor")
        verbose_name_plural = _("Actors")
        ordering = ["-created"]

    type = models.CharField(_("Actor Type"), max_length=25, default='character')


class Set(Element):
    class Meta:
        verbose_name = _("Set")
        verbose_name_plural = _("Sets")
        ordering = ["-created"]

    type = models.CharField(_("Set Type"), max_length=25, default='interaction')
    method = models.CharField(_("Set Method"), help_text=_("Union or Intersection"), max_length=1, default='I')
    actors = models.ManyToManyField('Actor', related_name='parent_products')


class RelativePosition(BaseModel, RawTitle):
    class Meta:
        verbose_name = _("Relative Position")
        verbose_name_plural = _("Relative Positions")
        ordering = ["-created"]
        default_related_name = 'relative_positions'

    type = models.CharField(_("Position Type"), max_length=25, default='')
    place = models.ForeignKey('Actor')


class Alias(BaseModel, RawTitle):
    class Meta:
        verbose_name = _("Alias")
        verbose_name_plural = _("Aliases")
        ordering = ["-created"]
        default_related_name = 'aliases'

    element = models.ForeignKey('Element')
    type = models.CharField(_("Alias Type"), max_length=25, default='')

