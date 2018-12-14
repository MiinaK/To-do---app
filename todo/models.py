from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)

class Todo(models.Model):
    text = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, 
        related_name='todos', 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE
        )


