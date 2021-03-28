from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from users.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Employee(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    enrollment = models.CharField(_('num empleado'), max_length=10, unique=True)
    anti = models.IntegerField(default=0, blank=True, null=True)
    CURP = models.CharField(default="", max_length=20, blank=True, null=True)
    NSS = models.CharField(default="", max_length=11, blank=True, null=True)
    area = models.CharField(default="", max_length=50, blank=True, null=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.enrollment

class Request(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    type = models.CharField(default="", max_length=30, blank=True, null=True)  # Tramite
    description = models.CharField(default="", max_length=50, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.type
    