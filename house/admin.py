from django.contrib import admin
from django.apps import apps

from .models import *

# Register your models here.
app = apps.get_app_config('house')
for model in app.models.values():
    name = model.__name__
    if name in ('Package', 'Ticket'):
        continue
    admin.site.register(model)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('arrive_datetime', 'picked_up',)
