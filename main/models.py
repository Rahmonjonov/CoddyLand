from typing import Any
from django.db import models
    
    
class Article(models.Model):
    img = models.ImageField(upload_to='article', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name