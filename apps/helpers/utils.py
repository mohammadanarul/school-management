from django.db import models
from django.utils.translation import gettext_lazy as _


class InstituteTypes(models.IntegerChoices):
    PRIMARY = 1, _("Primary")
    SECONDARY = 2, _("Secondary")


class UserRoles(models.IntegerChoices):
    ADMIN = 1, _("Admin")
    STUDENT = 2, _("Student")
    HEAD_TEACHER = 3, _("Head Teacher")
    HEAD_ASSISTANT_HEAD_TEACHER = 4, _("Assistant Head Teacher")
    ASSISTANT_HEAD_TEACHER = 5, _("Assistant Teacher")
    STAFF = 6, _("Staff")


class Genders(models.IntegerChoices):
    MALE = 1, _("Male")
    FEMALE = 2, _("Female")
    OTHERS = 3, _("Others")


class BloodGroups(models.IntegerChoices):
    A_PLUS = 1, _("A+")
    A_MINUS = 2, _("A-")
    B_PLUS = 3, _("B+")
    B_MINUS = 4, _("B-")
    O_PLUS = 5, _("O+")
    AB_PLUS = 5, _("AB+")
    AB_MINUS = 5, _("AB-")
