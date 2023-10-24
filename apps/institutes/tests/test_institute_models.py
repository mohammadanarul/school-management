import pytest
from apps.helpers.utils import SubjectType

pytestmark = pytest.mark.django_db


class TestInstituteModel:
    def test_str_return(self, institute_factory):
        institute = institute_factory.create()
        assert institute.__str__() == f"{institute.institute_code}-{institute.name}"


class TestSubjectModel:
    def test_property_subject_type_name(self, subject_factory):
        subject = subject_factory.create()
        assert subject.subject_type_name == dict(SubjectType.choices).get(subject.subject_type)

    def test_str_return(self, subject_factory):
        subject = subject_factory.create()
        assert subject.__str__() == f"{subject.code}-{subject.name}"


class TestKlassModel:
    def test_return_str(self, klass_factory):
        klass = klass_factory.create()
        assert klass.__str__() == klass.name


class TestSessionModel:
    def test_return_str(self, session_factory):
        session = session_factory.create()
        assert session.__str__() == session.year
