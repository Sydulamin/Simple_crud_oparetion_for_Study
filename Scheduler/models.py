from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name