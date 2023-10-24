import factory
from apps.exams.models import Exam
from apps.institutes.tests.factories import InstituteFactory, SessionFactory


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
