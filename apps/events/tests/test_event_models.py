import pytest

pytestmark = pytest.mark.django_db


class TestEventModel:
    def test_return_str(self, event_factory):
        event = event_factory.create()
        assert event.__str__() == event.name
