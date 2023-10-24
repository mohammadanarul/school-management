import pytest

pytestmark = pytest.mark.django_db


class TestRoutineModel:
    def test_return_str(self, routine_factory):
        routine = routine_factory.create()
        assert routine.__str__() == routine.klass.name
