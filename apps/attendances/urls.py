from rest_framework import routers
from apps.attendances.views import AttendanceModelViewSet, StaffAttendanceModelViewSet, ExamAttendanceModelViewSet

attendace_routers = routers.DefaultRouter()

attendace_routers.register("attendances", AttendanceModelViewSet, basename="attendaces")
attendace_routers.register("staff-attedances", StaffAttendanceModelViewSet, basename="staff-attedances")
attendace_routers.register("exam-attendances", ExamAttendanceModelViewSet, basename="exam-attendances")

urlpatterns = [] + attendace_routers.urls
