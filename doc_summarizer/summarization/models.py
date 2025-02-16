from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    date_of_creation = models.DateTimeField()
