from django.db import models
from datetime import date

class Task(models.Model):
    title = models.CharField(max_length=100)
    description =models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, default='pending')

    def is_overdue(self):
        return date.today() > self.due_date

    def display_status(self):
        if self.is_overdue() and self.status == 'complete':
            return 'overdue'
        return 'complete' if self.status == 'complete' else 'pending'
    
    def __str__(self):
        return self.title


# Create your models here.
