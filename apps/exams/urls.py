from rest_framework import routers
from apps.exams.views import ExamModelViewSet, ExamResultModelViewSet


router = routers.DefaultRouter()

router.register("exams", ExamModelViewSet, basename="exams")
router.register("exam_results", ExamResultModelViewSet, basename="exam_results")

urlpatterns = [] + router.urls
