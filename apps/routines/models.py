from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.helpers.models import BaseEntity
from apps.helpers.utils import DayChoices
from apps.users.models import Teacher
from apps.institutes.models import Klass, Subject


class Routine(BaseEntity):
    klass = models.ForeignKey(Klass, verbose_name=_("klass"), on_delete=models.CASCADE, db_index=True)
    teacher = models.ForeignKey(Teacher, verbose_name=_("teacher"), on_delete=models.CASCADE, db_index=True)
    subject = models.ForeignKey(Subject, verbose_name=_("subject"), on_delete=models.CASCADE)
    day = models.CharField(_("day"), choices=DayChoices.choices, db_index=True)
    time = models.TimeField(verbose_name=_("time"))

    def __str__(self) -> str:
        return self.klass.name
