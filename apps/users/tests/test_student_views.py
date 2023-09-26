import pytest
from django.test import TestCase


@pytest.fixture
def json_format():
    return {}


def test_qequal(json_format):
    assert json_format == {}
