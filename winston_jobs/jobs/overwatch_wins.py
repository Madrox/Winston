from winston_jobs.base import Job
import requests
import json


class OverwatchWins(Job):
    # Methods:
    # - self.val(key) -- get value for key. Way to persist data between jobs.
    # - self.set_val(key, val) -- set value for key.
    # - self.history -- a django queryset of times this job has run.

    def run(self):
        "Do stuff"
        wins = self.val("wins")
        if wins is None:
            wins = 0
        UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        data = json.loads(requests.get(
            'https://owapi.net/api/v3/u/itmightbedave/blob?platform=psn',
            headers={
                'User-Agent': UA,
            }
        ).text)
        new_wins = data['any']['stats']['competitive']['overall_stats']['wins']
        new_wins += data['any']['stats']['quickplay']['overall_stats']['wins']

        if new_wins > wins:
            self.make_event("Congratulations on the Overwatch win!")
        self.set_val("wins", new_wins)
