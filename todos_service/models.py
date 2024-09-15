from django.db import models

# Create your models here.
class Todo(models.Model):
    """
    Model representing a todo item.
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Additional fields can be added here if needed

    def __str__(self): 
        return f"{self.title} - {'Completed' if self.completed else 'Pending'}"