from rest_framework import routers
from apps.routines.views import RoutineModelViewSet

routine_routers = routers.DefaultRouter()
routine_routers.register("routines", RoutineModelViewSet, basename="routines")

urlpatterns = [] + routine_routers.urls
