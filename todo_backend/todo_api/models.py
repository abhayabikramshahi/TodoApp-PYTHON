from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=200)
    category = models.CharField(max_length=50, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task

    class Meta:
        ordering = ['-created_at']
