import pytest

pytestmark = pytest.mark.django_db


class TestExamModel:
    def test_return_str(self, exam_factory):
        exam = exam_factory.create()
        assert exam.__str__() == f"{exam.session.year}-{exam.get_status_display()}"
