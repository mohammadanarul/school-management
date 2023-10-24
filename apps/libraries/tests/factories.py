import factory
from faker import Faker
from django.core.files.base import ContentFile
from apps.libraries.models import Library, Book
from apps.institutes.tests.factories import InstituteFactory

fake = Faker()


class LibraryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Library

    institute = factory.SubFactory(InstituteFactory)
    name = fake.name()
    established_date = fake.date()


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    library = factory.SubFactory(LibraryFactory)
    writer_name = fake.name()
    name = fake.name()
    cover_image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 300, "height": 320}),
            "banner-example.jpg",
        )
    )
    pdf_file = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.FileField()._make_data({"width": 300, "height": 320}),
            f"{fake.name()}-nothing.pdf",
        )
    )
    page_number = fake.random_int()
    publication = fake.name()
