from django.db import models

class Restaurant(models.Model):
    is_open = models.BooleanField(default=True)
    location = models.CharField(max_length=255)
    metro = models.CharField(max_length=255)
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()

    def __str__(self):
        return self.location



