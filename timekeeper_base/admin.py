from django.contrib import admin

# Register your models here.
from .models import (Timeline,
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


admin.site.register(Timeline)
admin.site.register(Time)
admin.site.register(TimeLink)
admin.site.register(TimeKeeper)
admin.site.register(EventRule)
admin.site.register(Event)
admin.site.register(Action)
admin.site.register(Activity)
admin.site.register(Perspective)
admin.site.register(Element)
admin.site.register(Actor)
admin.site.register(Product)
admin.site.register(RelativePosition)
admin.site.register(Alias)
