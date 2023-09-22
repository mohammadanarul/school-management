from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.helpers.models import BaseEntity
from apps.helpers.utils import AttendanceType
from apps.users.models import Student, Staff
from apps.institutes.models import Institute, Session, Subject
from apps.exams.models import Exam


class Attendance(BaseEntity):
    institute = models.ForeignKey(
        Institute, verbose_name=_("institute"), on_delete=models.CASCADE
    )
    session = models.ForeignKey(
        Session,
        verbose_name=_("session"),
        on_delete=models.RESTRICT,
        related_name="attentdances",
    )
    student = models.ForeignKey(
        Student, verbose_name=_("student"), on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject, verbose_name=_("session"), on_delete=models.RESTRICT
    )
    status = models.SmallIntegerField(_("status"), choices=AttendanceType.choices)

    @property
    def status_name(self):
        return self.get_status_display()


class StaffAttendance(BaseEntity):
    institute = models.ForeignKey(
        Institute, verbose_name=_("institute"), on_delete=models.CASCADE
    )
    staff = models.ForeignKey(
        Staff,
        verbose_name=_("staff"),
        on_delete=models.CASCADE,
    )
    entry_time = models.DateTimeField(auto_now_add=True)
    lead_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.staff.mobile_number


class ExamAttendance(BaseEntity):
    institute = models.ForeignKey(
        Institute, verbose_name=_("institute"), on_delete=models.CASCADE
    )
    session = models.ForeignKey(
        Session,
        verbose_name=_("session"),
        on_delete=models.RESTRICT,
    )
    exam = models.ForeignKey(
        Exam, verbose_name=_("exam"), on_delete=models.RESTRICT
    )
    student = models.ForeignKey(
        Student, verbose_name=_("student"), on_delete=models.CASCADE
    )
    gpa = models.FloatField(_("gpa"), null=True, blank=True)
    subject = models.ForeignKey(
        Subject, verbose_name=_("session"), on_delete=models.RESTRICT
    )
    status = models.SmallIntegerField(_("status"), choices=AttendanceType.choices)

    @property
    def status_name(self):
        return self.get_status_display()
