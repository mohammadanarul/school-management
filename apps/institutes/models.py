from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.helpers.models import BaseEntity
from apps.helpers.utils import InstituteTypes, SubjectType

# from apps.users.models import Student


class Institute(BaseEntity):
    name = models.CharField(_("name"), max_length=255)
    established_year = models.SmallIntegerField(_("established year"))
    president = models.CharField(_("president"), max_length=200)
    principal = models.CharField(_("principal"), max_length=255)
    website_domain_address = models.URLField(_("website domain address"))
    email = models.EmailField(_("email"), max_length=255)
    address = models.CharField(_("address"), max_length=255)
    phone_number_1 = models.CharField(_("phone number one"), max_length=14)
    phone_number_2 = models.CharField(_("phone number two"), max_length=14)
    image = models.ImageField(_("image"), upload_to="institute-images/")
    logo = models.ImageField(_("logo"), upload_to="institute-logo-images/")
    eiin_number = models.CharField(_("eiin_number"), max_length=100)
    institute_code = models.CharField(_("code"), max_length=100)
    type = models.SmallIntegerField(
        _("type"), choices=InstituteTypes.choices, default=InstituteTypes.PRIMARY
    )
    institute_about = models.TextField(
        _("about"),
    )

    def __str__(self):
        return f"{self.institute_code}-{self.name}"


class Subject(BaseEntity):
    institute = models.ForeignKey(
        Institute, verbose_name=_("institute"), on_delete=models.CASCADE
    )
    name = models.CharField(_("name"), max_length=150)
    code = models.SmallIntegerField(_("code"))
    type = models.SmallIntegerField(
        _("type"), choices=SubjectType.choices, default=SubjectType.MANDATORY
    )

    @property
    def type_name(self):
        return self.get_type_display()

    def __str__(self):
        return f"{self.code}-{self.name}"


class Klass(BaseEntity):
    institute = models.ForeignKey(
        Institute, verbose_name=_("institute"), on_delete=models.CASCADE
    )
    name = models.CharField(_("name"), max_length=100)
    seats = models.SmallIntegerField(_("seats"))
    subjects = models.ManyToManyField(
        Subject, verbose_name=_("subjects"), related_name="klass_list"
    )

    def __str__(self):
        return self.name


class Session(BaseEntity):
    institute = models.ForeignKey(
        Institute, verbose_name=_("institute"), on_delete=models.CASCADE
    )
    klass = models.ForeignKey(
        Klass,
        verbose_name=_("klass"),
        on_delete=models.CASCADE,
        related_name="sessions",
    )
    students = models.ManyToManyField(
        "users.Student", verbose_name=_("students"), related_name="sessions"
    )
    year = models.SmallIntegerField(_("year"))

    def __str__(self):
        return self.year
