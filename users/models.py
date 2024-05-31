from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
    )

    BRANCH_CHOICES = (
        ('B.Tech', 'B.Tech'),
        ('MBA', 'MBA'),
        ('BSC', 'BSC'),
        # Add more branches as needed
    )

    DEPARTMENT_CHOICES = (
        ('cse', 'Computer Science and Engineering'),
        ('ece', 'Electronics and Communication Engineering'),
        ('eee', 'Electrical and Electronics Engineering'),
        ('mech', 'Mechanical Engineering'),
        # Add more departments as needed
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    branch = models.CharField(max_length=100, choices=BRANCH_CHOICES, blank=True, null=True)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.username
