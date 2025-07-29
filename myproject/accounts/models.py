from django.contrib.auth.models import AbstractUser
from django.db import models

CLUSTER_CHOICES = [
    ('government', 'Government'),
    ('private', 'Private'),
    ('ngo', 'NGO'),
    ('individual', 'Individual'),
]

class CustomUser(AbstractUser):
    user = models.AutoField(primary_key=True)  # explicitly define primary key
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    cluster = models.CharField(max_length=20, choices=CLUSTER_CHOICES)

    # Remove username field (use email as username)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number', 'cluster']

    def __str__(self):
        return self.email