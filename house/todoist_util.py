import requests
from django.conf import settings


def quick_add_task(text, note='', reminder=''):
    requests.post(
        'https://todoist.com/API/v7/quick/add',
        data={
            'token': settings.TODOIST_TOKEN,
            'text': text,
            'note': note,
            'reminder': reminder
        }
    )
