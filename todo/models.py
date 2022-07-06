import uuid
from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, verbose_name="ID", editable=False)
    title = models.CharField(max_length=70, default="Todo")
    body = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title