from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):

    def _create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError('User must input email')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password, **extra_fields)



