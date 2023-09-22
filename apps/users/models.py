from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from apps.helpers.utils import (
    UserRoles,
    Genders,
    BloodGroups,
    SalaryGrade,
    CertificateType,
)
from apps.helpers.regex_validators import phone_number_validator
from apps.users.managers import CustomUserManager
from apps.helpers.models import BaseEntity
from apps.institutes.models import Subject


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    mobile_number = models.CharField(
        _("username"),
        validators=[phone_number_validator],
        max_length=150,
        unique=True,
        help_text=_("Mobile Number"),
        error_messages={
            "unique": _("A user with that mobile number already exists."),
        },
        db_index=True,
    )
    email = models.EmailField(
        _("email address"), unique=True, blank=True, db_index=True
    )
    age = models.SmallIntegerField(_("age"))
    gender = models.SmallIntegerField(
        _("gender"), choices=Genders.choices, default=Genders.MALE
    )
    blood_group = models.SmallIntegerField(
        choices=BloodGroups.choices, default=BloodGroups.AB_PLUS
    )
    role = models.SmallIntegerField(choices=UserRoles.choices, default=UserRoles.ADMIN)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "mobile_number"
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "age"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.mobile_number


class Student(BaseEntity):
    user = models.OneToOneField(
        User, verbose_name=_("user"), on_delete=models.CASCADE, related_name="students"
    )
    father_name = models.CharField(_("father name"), max_length=250)
    mother_name = models.CharField(_("mother name"), max_length=250)
    image = models.ImageField(
        "profile image",
        help_text=_("Image must will be passport size"),
    )


class Staff(BaseEntity):
    user = models.OneToOneField(
        User, verbose_name=_("user"), on_delete=models.CASCADE, related_name="teachers"
    )
    father_name = models.CharField(_("father name"), max_length=250)
    mother_name = models.CharField(_("mother name"), max_length=250)
    image = models.ImageField(
        "profile image",
        help_text=_("Image must will be passport size"),
    )
    subjects = models.ManyToManyField(Subject, verbose_name=_("subjects"), blank=True)
    salary_grade = models.IntegerField(_("salary"), choices=SalaryGrade.choices)
    regain_date = models.DateField(_("regain date"), null=True, blank=True)

    @property
    def salary_grade_name(self):
        return self.get_salary_grade_display()


class Certificate(BaseEntity):
    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name="certificates",
    )
    type = models.SmallIntegerField(_("type"), choices=CertificateType.choices)
    gpa = models.FloatField(_("GPA"))
    session_year = models.SmallIntegerField(_("session year"))
    image = models.ImageField(
        _("image"), help_text="Certificate Image", upload_to="certificates"
    )

    @property
    def type_name(self):
        return self.get_type_display()
