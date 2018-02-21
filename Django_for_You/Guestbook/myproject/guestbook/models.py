from django.db import models
from django.utils import timezone
# Create your models here.
class Comment(models.Model):
    #I want who wrote the comment and the comment itself
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return '<Name:{}, ID:{}>'.format(self.name,self.id)