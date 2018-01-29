from django.contrib import admin

# Register your models here.
from .models import (Timeline, Axis, Position,
                     Note,
                     TimeKeeper)

admin.site.register(Timeline)
admin.site.register(Axis)
admin.site.register(Position)
admin.site.register(Note)
admin.site.register(TimeKeeper)
