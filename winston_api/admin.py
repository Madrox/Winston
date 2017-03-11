from django.contrib import admin
from django.apps import apps

from .models import *

# Register your models here.
app = apps.get_app_config('winston_api')
for model in app.models.values():
    name = model.__name__
    if name in ('Event', 'Ticket'):
        continue
    admin.site.register(model)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'message', 'scheduled_time', 'speak', 'announced')
