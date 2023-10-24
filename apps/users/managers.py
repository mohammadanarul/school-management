from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.query import QuerySet
from apps.helpers.utils import UserRoles


class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, mobile_number, email, age, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
            email=self.normalize_email(email),
            age=age,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, mobile_number, email, age, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            first_name,
            last_name,
            mobile_number,
            email,
            age=age,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class HeadTeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        return super().get_queryset(*args, **kwargs).filter(role=UserRoles.HEAD_TEACHER)


class AssistantHeadTeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        return super().get_queryset(*args, **kwargs).filter(role=UserRoles.ASSISTANT_HEAD_TEACHER)


class AssistantTeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        return super().get_queryset(*args, **kwargs).filter(role=UserRoles.ASSISTANT_TEACHER)


class StaffManager(models.Manager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        return super().get_queryset(*args, **kwargs).filter(role=UserRoles.STAFF)


class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        return super().get_queryset(*args, **kwargs).filter(role=UserRoles.STUDENT)
