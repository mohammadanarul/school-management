from django.urls import path
from rest_framework import routers
from apps.institutes.views import (
    InstituteModelViewSet,
    SubjectModelViewSet,
    KlassModelViewSet,
    SessionModelViewSet,
)

router = routers.DefaultRouter()

router.register("institutes", InstituteModelViewSet, basename="institutes")
router.register("subjects", SubjectModelViewSet, basename="subjects")
router.register("klass", KlassModelViewSet, basename="klass")
router.register("sessions", SessionModelViewSet, basename="sessions")

urlpatterns = [] + router.urls
