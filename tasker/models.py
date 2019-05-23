from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=128, null=False)
    details = models.CharField(max_length=256)
    creation_date = models.DateTimeField(auto_now=True)

