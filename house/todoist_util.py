import requests
from django.conf import settings


def quick_add_task(text, note=''):
    requests.post(
        'https://todoist.com/API/v7/quick/add',
        data={
            'token': settings.TODOIST_TOKEN,
            'text': text,
            'note': note
        }
    )
