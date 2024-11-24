from django.db import models


class Сatalog(models.Model):
    name = models.CharField(max_length=52)


