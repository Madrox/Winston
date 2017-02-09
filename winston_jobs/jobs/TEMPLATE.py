from winston_jobs.base import Job

# Copy this file into the jobs folder to use as the basis of a new job


class YOUR_JOB_NAME(Job):
    # Methods:
    # - self.val(key) -- get value for key. Way to persist data between jobs.
    # - self.set_val(key) -- set value for key.
    # - self.history -- a django queryset of times this job has run.

    def run(self):
        "Do stuff"
        # print "Work work work"
        return
