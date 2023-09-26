import pytest
from pytest_factoryboy import register
from apps.exams.tests.factories import ExamFactory

register(ExamFactory)
