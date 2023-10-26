import factory
from apps.users.tests.factories import StudentFactory
from apps.exams.models import Exam, ExamResult
from apps.institutes.tests.factories import InstituteFactory, SessionFactory, SubjectFactory


class ExamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Exam

    institute = factory.SubFactory(InstituteFactory)
    session = factory.SubFactory(SessionFactory)
    exam_type = 1
    status = 1

    @factory.post_generation
    def students(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.students.set(extracted)


class ExamResultFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ExamResult

    exam = factory.SubFactory(ExamFactory)
    student = factory.SubFactory(StudentFactory)
    subject = factory.SubFactory(SubjectFactory)
    gpa = 3.20
