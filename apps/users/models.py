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
from apps.users.managers import (
    CustomUserManager,
    HeadTeacherManager,
    AssistantHeadTeacherManager,
    AssistantTeacherManager,
    StudentManager,
    StaffManager,
)


class User(AbstractBaseUser, PermissionsMixin):
    default_role = UserRoles.ADMIN
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    father_name = models.CharField(_("father name"), max_length=250)
    mother_name = models.CharField(_("mother name"), max_length=250)
    image = models.ImageField(
        "image",
        help_text=_("Image must will be passport size"),
    )
    mobile_number = models.CharField(
        _("mobile number"),
        validators=[phone_number_validator],
        max_length=150,
        unique=True,
        help_text=_("Mobile Number"),
        error_messages={
            "unique": _("A user with that mobile number already exists."),
        },
        db_index=True,
    )
    email = models.EmailField(_("email address"), unique=True, blank=True, db_index=True)
    age = models.SmallIntegerField(_("age"))
    gender = models.SmallIntegerField(_("gender"), choices=Genders.choices, default=Genders.MALE)
    blood_group = models.SmallIntegerField(choices=BloodGroups.choices, default=BloodGroups.AB_PLUS)
    role = models.SmallIntegerField(choices=UserRoles.choices, default=default_role)
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
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "mobile_number"
    REQUIRED_FIELDS = ["first_name", "last_name", "father_name", "mother_name", "email", "age"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.role = self.default_role
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.mobile_number


class StaffProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE, related_name="staff_profile")
    subjects = models.ManyToManyField("institutes.Subject", verbose_name=_("subjects"), blank=True)
    salary_grade = models.IntegerField(_("salary"), choices=SalaryGrade.choices)
    regain_date = models.DateField(_("regain date"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="+", null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="+", null=True, blank=True)

    @property
    def salary_grade_name(self):
        return self.get_salary_grade_display()


class Student(User):
    default_role = UserRoles.STUDENT

    objects = StudentManager()

    class Meta:
        proxy = True


class HeadTeacher(User):
    default_role = UserRoles.HEAD_TEACHER
    objects = HeadTeacherManager()

    class Meta:
        proxy = True


class AssistandHeadTeacher(User):
    default_role = UserRoles.ASSISTANT_HEAD_TEACHER

    objects = AssistantHeadTeacherManager()

    class Meta:
        proxy = True


class Teacher(User):
    default_role = UserRoles.ASSISTANT_TEACHER

    objects = AssistantTeacherManager()

    class Meta:
        proxy = True


class Staff(User):
    default_role = UserRoles.STAFF

    objects = StaffManager()

    class Meta:
        proxy = True


class Certificate(models.Manager):
    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name="certificates",
    )
    certificate_type = models.SmallIntegerField(_("type"), choices=CertificateType.choices)
    gpa = models.FloatField(_("GPA"))
    session_year = models.SmallIntegerField(_("session year"))
    image = models.ImageField(_("image"), help_text="Certificate Image", upload_to="users/certificates/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="+", null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="+", null=True, blank=True)

    @property
    def certificate_type_name(self):
        return self.get_certificate_type_display()

    def __str__(self) -> str:
        return f"{self.user.mobile_number}-{self.certificate_type_name}"
