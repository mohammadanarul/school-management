import factory
from apps.helpers.utils import AttendanceType
from apps.users.tests.factories import StudentFactory, UserFactory
from apps.attendances.models import Attendance, StaffAttendance, ExamAttendance
from apps.institutes.tests.factories import InstituteFactory, SubjectFactory, KlassFactory
from apps.exams.tests.factories import ExamFactory


class AttendanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attendance

    institute = factory.SubFactory(InstituteFactory)
    klass = factory.SubFactory(KlassFactory)
    student = factory.SubFactory(StudentFactory)
    subject = factory.SubFactory(SubjectFactory)
    status = AttendanceType.PRESENT


class StaffAttendanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StaffAttendance

    institute = factory.SubFactory(InstituteFactory)
    staff_user = factory.SubFactory(UserFactory)
    status = AttendanceType.PRESENT


class ExamAttendanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ExamAttendance

    institute = factory.SubFactory(InstituteFactory)
    klass = factory.SubFactory(KlassFactory)
    exam = factory.SubFactory(ExamFactory)
    student = factory.SubFactory(StudentFactory)
    subject = factory.SubFactory(SubjectFactory)
    status = AttendanceType.PRESENT
