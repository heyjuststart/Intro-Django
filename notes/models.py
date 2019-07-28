from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

# new model with a foreign key from django's builtin user model
class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
