import factory
from django.core.files.base import ContentFile
from faker import Faker
from apps.events.models import Event

fake = Faker()


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    session_year = int(fake.year())
    name = fake.name()
    date = fake.date()
    banner = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 300, "height": 320}),
            "banner-example.jpg",
        )
    )
    group_image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data({"width": 300, "height": 320}),
            "banner-example.jpg",
        )
    )
    cost_balance = fake.random_int()
