import pytest

pytestmark = pytest.mark.django_db


class TestAttendanceModel:
    def test_property_status_name(self, attendance_factory):
        attendance = attendance_factory.create()
        assert attendance.status_name == attendance.get_status_display()

    def test_return_str(self, attendance_factory):
        attendance = attendance_factory.create()
        assert attendance.__str__() == f"{attendance.student.mobile_number}-{attendance.status_name}"


class TestStaffAttendanceModel:
    def test_return_str(self, staff_attendance_factory):
        attendance = staff_attendance_factory.create()
        assert attendance.__str__() == f"{attendance.staff_user.mobile_number}-{attendance.get_status_display()}"


class TestExamAttendanceModel:
    def test_property_status_name(self, exam_attendance_factory):
        attendance = exam_attendance_factory.create()
        assert attendance.status_name == attendance.get_status_display()

    def test_return_str(self, exam_attendance_factory):
        attendance = exam_attendance_factory.create()
        assert attendance.__str__() == f"{attendance.student.mobile_number}-{attendance.status_name}"
