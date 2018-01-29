from django.utils.translation import ugettext_lazy as _

from timekeeperapi.mixins.models import *


class BaseModel(TimeStamped, Ownable):
    class Meta:
        abstract = True


class Axis(BaseModel):
    class Meta:
        verbose_name = _("Axis")
        verbose_name_plural = _("Axe")
        ordering = ["-created"]

    maximum_position = models.ForeignKey("Position", related_name='+')
    minimum_position = models.ForeignKey("Position", related_name='+')


class Position(BaseModel, RawTitle):
    class Meta:
        verbose_name = _("Position")
        verbose_name_plural = _("Positions")
        ordering = ["-created"]
        default_related_name = 'positions'

    axis = models.ForeignKey('Axis')
    value = models.FloatField(_('Value'), default=0, db_index=True)

class Note(BaseModel):
    class Meta:
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")
        ordering = ["-created"]

    positions = models.ManyToManyField('Position')


class Timeline(BaseModel, RawTitle):
    class Meta:
        verbose_name = _('Timeline')
        verbose_name_plural = _('Timelines')
        ordering = ["-created"]
        default_related_name = 'timelines'

    axis = models.ForeignKey('Axis', blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            self.axis
        except Axis.DoesNotExist:
            self.axis = Axis.objects.create()
        return super(Timeline, self).save(*args, **kwargs)


class TimeKeeper(BaseModel):
    class Meta:
        verbose_name = _("Time Keeper")
        verbose_name_plural = _("Time Keepers")
        ordering = ["-created"]
        default_related_name = 'time_keepers'

    timeline = models.ForeignKey('Timeline', blank=True, null=True)