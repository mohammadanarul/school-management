from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAdminUser
from apps.exams.models import Exam
from apps.exams.serializers import ExamSerializer


class ExamModelViewSet(ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
