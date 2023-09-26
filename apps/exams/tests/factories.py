import factory
from faker import Faker
from apps.exams.models import Exam


class ExamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Exam
