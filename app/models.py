from django.db import models

# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=200)
    url = models.FileField(upload_to='uploads/%y')

    def __str__(self):
        return self.name