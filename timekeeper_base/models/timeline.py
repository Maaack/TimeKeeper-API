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

    timeline = models.ForeignKey('Timeline')
    time = models.ForeignKey('Time')
    order = models.IntegerField(_("Order"), default=0)


class TimeKeeper(BaseModel):
    class Meta:
        verbose_name = _("Time Keeper")
        verbose_name_plural = _("Time Keepers")
        ordering = ["-created"]

    timeline = models.ForeignKey('Timeline')


class EventRule(BaseModel, RawText):
    class Meta:
        verbose_name = _("Event Rule")
        verbose_name_plural = _("Event Rules")
        ordering = ["-created"]

    original_time = models.ForeignKey('Time', null=True)
    repeats = models.BooleanField(_("Repeats"), default=False)
    occurrences = models.IntegerField(_("Occurrences"), default=1)


class Event(BaseModel, RawText):
    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ["-created"]

    event_rule = models.ForeignKey('EventRule')
    time = models.ForeignKey('Time')
    place = models.ForeignKey('RelativePosition')
    action = models.ForeignKey('Action')


class Action(BaseModel):
    class Meta:
        verbose_name = _("Action")
        verbose_name_plural = _("Actions")
        ordering = ["-created"]

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


class Product(Element):
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["-created"]

    elements = models.ManyToManyField('Element', related_name='parent_products')
    type = models.CharField(_("Product Type"), max_length=25, default='interaction')


class RelativePosition(BaseModel, RawTitle):
    class Meta:
        verbose_name = _("Relative Position")
        verbose_name_plural = _("Relative Positions")
        ordering = ["-created"]

    type = models.CharField(_("Position Type"), max_length=25, default='')
    place = models.ForeignKey('Actor')


class Alias(BaseModel, RawTitle):
    class Meta:
        verbose_name = _("Alias")
        verbose_name_plural = _("Aliases")
        ordering = ["-created"]

    actor = models.ForeignKey('Actor')


