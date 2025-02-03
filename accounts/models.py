# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    object_repr = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.timestamp} - {self.user}: {self.action}"
