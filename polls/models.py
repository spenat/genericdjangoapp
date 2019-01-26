from django.db import models


class Thumb(models.Model):
    image_src = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
