import factory
from faker import Faker
from django.core.files.base import ContentFile
from apps.helpers.helpers import bd_number_generator
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
    phone_number_1 = bd_number_generator()
    phone_number_2 = bd_number_generator()
    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 20, "height": 25}),
            "banner-example.jpg",
        )
    )
    logo = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 20, "height": 25}),
            "banner-example.jpg",
        )
    )
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

    @factory.post_generation
    def subjects(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for subject in extracted:
                self.subjects.add(subject)


class SessionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Session

    institute = factory.SubFactory(InstituteFactory)
    klass = factory.SubFactory(KlassFactory)
    year = fake.year()

    @factory.post_generation
    def students(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.students.set(extracted)
