import todoist
from django.conf import settings


def quick_add_task(self, text, note=''):
    api = todoist.TodoistAPI(settings.TODOIST_TOKEN)
    api.quick.add(text, note=note)
