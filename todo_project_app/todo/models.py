from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    class Meta:
        app_label = 'todo'
