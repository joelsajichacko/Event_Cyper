from django.db import models

# Create your models here.


class Events(models.Model):
    event_title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    time = models.DateTimeField()
    date = models.DateField()
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.event_title
