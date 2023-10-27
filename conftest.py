import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import Permission, Group
from apps.institutes.tests.factories import InstituteFactory, SubjectFactory, KlassFactory, SessionFactory
from apps.exams.tests.factories import ExamFactory, ExamResultFactory
from apps.events.tests.factories import EventFactory
from apps.users.tests.factories import UserFactory, StudentFactory, StaffFactory, StaffProfileFactory, TeacherFactory
from apps.addresses.tests.factories import (
    CountryFactory,
    DivisionFactory,
    DistrictFactory,
    SubDistrictFactory,
    UnionFactory,
    WardFactory,
    AddressFactory,
)
from apps.libraries.tests.factories import LibraryFactory, BookFactory
from apps.routines.tests.factories import RoutineFactory
from apps.attendances.tests.factories import AttendanceFactory, StaffAttendanceFactory, ExamAttendanceFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def admin_user_token(api_client):
    user = UserFactory()
    group, created = Group.objects.get_or_create(name="super-admin-group")
    for perm in Permission.objects.all():
        group.permissions.add(perm)
    group.user_set.add(user)
    group.save()
    # for perm in permissions:
    #     user.user_permissions.add(perm)
    # user.save()
    response = api_client.post(
        reverse("token_obtain_pair"),
        data={"mobile_number": user.mobile_number, "password": "password123"},
    )
    context = {
        "user": user,
        "access_token": response.data["access"],
        "refresh_token": response.data["refresh"],
    }
    return context


@pytest.fixture
def user_token(api_client):
    user = UserFactory()
    user.is_staff = False
    user.save()
    response = api_client.post(
        reverse("token_obtain_pair"),
        data={"mobile_number": user.mobile_number, "password": "password123"},
    )
    context = {
        "user": user,
        "access_token": response.data["access"],
        "refresh_token": response.data["refresh"],
    }
    return context


register(InstituteFactory)
register(SubjectFactory)
register(KlassFactory)
register(SessionFactory)
register(UserFactory)
register(StaffProfileFactory)
register(StaffFactory)
register(StudentFactory)
register(ExamFactory)
register(ExamResultFactory)
register(EventFactory)
register(CountryFactory)
register(DivisionFactory)
register(DistrictFactory)
register(SubDistrictFactory)
register(UnionFactory)
register(WardFactory)
register(AddressFactory)
register(LibraryFactory)
register(BookFactory)
register(RoutineFactory)
register(TeacherFactory)
register(AttendanceFactory)
register(StaffAttendanceFactory)
register(ExamAttendanceFactory)
