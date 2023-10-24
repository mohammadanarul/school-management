from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.helpers.models import BaseEntity
from apps.helpers.utils import ExamType, ExamStatus
from apps.users.models import Student
from apps.institutes.models import Institute, Session


class Exam(BaseEntity):
    institute = models.ForeignKey(Institute, verbose_name=_("institute"), on_delete=models.CASCADE)
    session = models.ForeignKey(
        Session,
        verbose_name=_("session"),
        on_delete=models.RESTRICT,
        related_name="exams",
    )
    students = models.ManyToManyField(Student, verbose_name=_("students"), related_name="my_exams")
    exam_type = models.SmallIntegerField(_("type"), choices=ExamType.choices)
    status = models.SmallIntegerField(_("status"), choices=ExamStatus.choices)

    def __str__(self):
        return f"{self.session.year}-{self.get_status_display()}"
