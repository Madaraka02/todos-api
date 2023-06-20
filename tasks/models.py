from django.db import models

# Create your models here.
class Task(models.Model):
    TASK_STATUS_CHOICES = (
    ("new", "new"),
    ("progress", "progress"),
    ("complete", "complete"),
    )
    description = models.TextField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(null=True, default='new', choices=TASK_STATUS_CHOICES, max_length=20)
    over_due = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Task {self.id}'
    
    