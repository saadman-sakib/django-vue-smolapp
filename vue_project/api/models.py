from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
    	return self.title
