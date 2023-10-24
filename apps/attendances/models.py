from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.helpers.models import BaseEntity
from apps.helpers.utils import AttendanceType
from apps.users.models import Student, User
from apps.institutes.models import Institute, Klass, Subject
from apps.exams.models import Exam


class Attendance(BaseEntity):
    institute = models.ForeignKey(Institute, verbose_name=_("institute"), on_delete=models.CASCADE)
    klass = models.ForeignKey(Klass, verbose_name=_("klass"), on_delete=models.CASCADE)
    student = models.ForeignKey(Student, verbose_name=_("student"), on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name=_("session"), on_delete=models.RESTRICT)
    status = models.SmallIntegerField(_("status"), choices=AttendanceType.choices)

    @property
    def status_name(self):
        return self.get_status_display()

    def __str__(self) -> str:
        return f"{self.student.mobile_number}-{self.status_name}"


class StaffAttendance(BaseEntity):
    institute = models.ForeignKey(Institute, verbose_name=_("institute"), on_delete=models.CASCADE)
    staff_user = models.ForeignKey(
        User,
        verbose_name=_("staff user"),
        on_delete=models.CASCADE,
    )
    status = models.SmallIntegerField(_("status"), choices=AttendanceType.choices)

    def __str__(self) -> str:
        return f"{self.staff_user.mobile_number}-{self.get_status_display()}"


class ExamAttendance(BaseEntity):
    institute = models.ForeignKey(Institute, verbose_name=_("institute"), on_delete=models.CASCADE)
    klass = models.ForeignKey(Klass, verbose_name=_("klass"), on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, verbose_name=_("exam"), on_delete=models.RESTRICT)
    student = models.ForeignKey(Student, verbose_name=_("student"), on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, verbose_name=_("session"), on_delete=models.RESTRICT)
    status = models.SmallIntegerField(_("status"), choices=AttendanceType.choices)

    @property
    def status_name(self):
        return self.get_status_display()

    def __str__(self) -> str:
        return f"{self.student.mobile_number}-{self.status_name}"
