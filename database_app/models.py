from django.db import models

# Create a model to bot
class Links(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    video_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name