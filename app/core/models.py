from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

  def create_user(self, email, password=None, **extra_fields):
    """Creates and saves a new user"""
    if not email:
      raise ValueError('Users must have an email address.')
    user = self.model(email=self.normalize_email(email), **extra_fields) #helperfunction from BUM
    user.set_password(password) #helper function from BaseUserManger
    user.save(using=self._db) #supporting multiple databases

    return user

  def create_superuser(self, email, password):
    """Creates and saves a new super user"""
    user = self.create_user(email, password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)

    return user

class User(AbstractBaseUser, PermissionsMixin):
  """Custom user model that supports using email instead of username"""
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserManager() #create new usermanager for the object

  USERNAME_FIELD = 'email'