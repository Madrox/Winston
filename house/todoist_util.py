import todoist
from django.conf import settings


def quick_add_task(text, note=''):
    api = todoist.TodoistAPI(settings.TODOIST_TOKEN)
    api.quick.add(text, note=note)
