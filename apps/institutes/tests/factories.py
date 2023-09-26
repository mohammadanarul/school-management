import factory
from faker import Faker
from apps.institutes.models import Institute, Subject, Klass, Session

fake = Faker()


class InstituteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Institute

    name = fake.name()
    established_year = fake.year()
    president = fake.name()
    principal = fake.name()
    website_domain_address = fake.url()
    email = fake.email()
    address = fake.address()
    phone_number_1 = fake.phone_number()
    phone_number_2 = fake.phone_number()
    image = fake.image()
    logo = fake.image()
    eiin_number = fake.random_int()
    institute_code = fake.random_int()
    institute_type = 1
    institute_about = fake.text()


class SubjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subject

    institute = factory.SubFactory(InstituteFactory)
    name = fake.name()
    code = fake.random_int()
    subject_type = 1


class KlassFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Klass

    institute = factory.SubFactory(InstituteFactory)
    name = fake.name()
    seats = fake.random_int()
    subjects = fake

    @factory.post_generation
    def subjects(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of subjects using bulk addition
        self.subjects.add(*extracted)


class SessionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Session

    institute = factory.SubFactory(InstituteFactory)
    klass = factory.SubFactory(KlassFactory)
    year = fake.year()

    @factory.post_generation
    def students(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of studensts using bulk addition
        self.students.add(*extracted)
