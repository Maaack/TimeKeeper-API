from django.contrib import admin

# Register your models here.
from .models import Axis, Position, Note, Timeline, TimeKeeper

admin.site.register(Timeline)
admin.site.register(Axis)
admin.site.register(Position)
admin.site.register(Note)
admin.site.register(TimeKeeper)
