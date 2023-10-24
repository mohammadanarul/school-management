import pytest

pytestmark = pytest.mark.django_db


class TestStaffProfileModel:
    def test_property_salary_grade_name(self, staff_profile_factory):
        profile = staff_profile_factory.create()
        assert profile.__str__() == profile.get_salary_grade_display()


class TestCertificateModel:
    def test_certificate_type_name(self, certificate_factory):
        certificate = certificate_factory.create()
        assert certificate.certificate_type == f"{certificate.user.mobile_number}-{certificate.certificate_type_name}"

    def test_return_str(self, certificate_factory):
        certificate = certificate_factory.create()
        assert certificate.__str__() == f"{certificate.user.mobile_number}-{certificate.certificate_type_name}"
