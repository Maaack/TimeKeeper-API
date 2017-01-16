from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Timeline)
admin.site.register(Time)
admin.site.register(TimeLink)
admin.site.register(TimeKeeper)
admin.site.register(Event)
