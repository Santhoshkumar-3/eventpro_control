from django.db import models
from categories.models import Category
from users.models import CustomUser

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255) 
    category = models.ForeignKey(Category, related_name='events', on_delete=models.CASCADE)
    student_organizer = models.ManyToManyField(CustomUser, related_name='student_events')
    staff_organizer = models.ManyToManyField(CustomUser, related_name='staff_events')


def __str__(self):
        return self.title