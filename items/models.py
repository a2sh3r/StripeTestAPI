from django.db import models


class Item(models.Model):
    name = models.TextField(default='blank item', blank=False, null=False)
    description = models.TextField(default='blank description', blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
