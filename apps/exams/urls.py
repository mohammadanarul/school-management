from rest_framework import routers
from apps.exams.views import ExamModelViewSet


router = routers.DefaultRouter()

router.register("exams", ExamModelViewSet, basename="exams")

urlpatterns = [] + router.urls
