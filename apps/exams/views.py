from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, DjangoModelPermissions
from apps.exams.models import Exam, ExamResult
from apps.exams.serializers import ExamSerializer, ExamResultSerializer


class ExamModelViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamResultModelViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [IsAuthenticated()]
        return [DjangoModelPermissions()]
