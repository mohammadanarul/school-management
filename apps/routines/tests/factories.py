import factory
from faker import Faker
from apps.routines.models import Routine
from apps.helpers.utils import DayChoices
from apps.users.tests.factories import TeacherFactory
from apps.institutes.tests.factories import KlassFactory, SubjectFactory

fake = Faker()


class RoutineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Routine

    klass = factory.SubFactory(KlassFactory)
    teacher = factory.SubFactory(TeacherFactory)
    subject = factory.SubFactory(SubjectFactory)
    day = DayChoices.SATURDAY
    time = fake.time()
