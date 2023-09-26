import pytest


@pytest.mark.django_db
def test_new_exam(exam_factory):
    print(exam_factory)
    assert True
