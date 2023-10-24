import factory
from faker import Faker
from django.core.files.base import ContentFile
from django.utils import timezone
from apps.users.models import User, Student, StaffProfile, Staff, Teacher
from apps.helpers.helpers import bd_number_generator

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = "mohammad"
    last_name = "anarul"
    father_name = fake.name()
    mother_name = fake.name()
    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 300, "height": 320}),
            "banner-example.jpg",
        )
    )
    mobile_number = factory.Sequence(lambda _: bd_number_generator())
    email = factory.Sequence(lambda _: fake.email())
    age = fake.random_int()
    gender = 1
    blood_group = 1
    is_staff = True
    is_active = True
    date_joined = timezone.now()
    password = factory.PostGenerationMethodCall("set_password", "password123")


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    first_name = "mohammad"
    last_name = "anarul"
    father_name = fake.name()
    mother_name = fake.name()
    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 300, "height": 320}),
            "banner-example.jpg",
        )
    )
    mobile_number = factory.Sequence(lambda _: bd_number_generator())
    email = factory.Sequence(lambda _: fake.email())
    age = fake.random_int()
    gender = 1
    blood_group = 1
    is_active = True
    date_joined = timezone.now()
    password = factory.PostGenerationMethodCall("set_password", "password123")


class TeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Teacher

    first_name = "mohammad"
    last_name = "anarul"
    father_name = fake.name()
    mother_name = fake.name()
    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 300, "height": 320}),
            "banner-example.jpg",
        )
    )
    mobile_number = factory.Sequence(lambda _: bd_number_generator())
    email = factory.Sequence(lambda _: fake.email())
    age = fake.random_int()
    gender = 1
    blood_group = 1
    is_active = True
    date_joined = timezone.now()
    password = factory.PostGenerationMethodCall("set_password", "password123")


class StaffProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StaffProfile

    user = factory.SubFactory("apps.users.tests.factories.StaffFactory", staff_profile=None)
    salary_grade = 1

    @factory.post_generation
    def subjects(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for subject in extracted:
                self.subjects.add(subject)


class StaffFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Staff

    first_name = "mohammad"
    last_name = "anarul"
    father_name = fake.name()
    mother_name = fake.name()
    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 300, "height": 320}),
            "banner-example.jpg",
        )
    )
    mobile_number = factory.Sequence(lambda _: bd_number_generator())
    email = factory.Sequence(lambda _: fake.email())
    age = fake.random_int()
    gender = 1
    role = 6
    blood_group = 1
    is_staff = True
    is_active = True
    date_joined = timezone.now()
    password = factory.PostGenerationMethodCall("set_password", "password123")
    staff_profile = factory.RelatedFactory(StaffProfileFactory, factory_related_name="user")
