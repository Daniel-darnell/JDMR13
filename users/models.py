from django.db import models
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
        email = models.EmailField(max_length=40, unique=True)
        first_name = models.CharField(max_length=30, blank=True)
        last_name = models.CharField(max_length=30, blank=True)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=True)
        date_joined = models.DateTimeField(default=timezone)

        objects = UserManager()

        USERNAME_FIELD ='email'
        REQUIRED_FIELDS = ['first_name', 'last_name']

        def save(self, *args,**kwargs):
            super(User, self).save(*args, **kwargs)
            return self 
                
