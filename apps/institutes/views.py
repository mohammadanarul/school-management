from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from apps.helpers.mixins import DeleteModelMixin, ModelViewSetMixin
from apps.institutes.models import Institute, Subject, Klass, Session
from apps.institutes.serializers import (
    InstituteSerializer,
    SubjectSerialiser,
    KlassSerializer,
    SessionSerializer,
)


class InstituteModelViewSet(DeleteModelMixin, ModelViewSetMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer

    def get_permissions(self):
        if self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAdminUser()]


class SubjectModelViewSet(DeleteModelMixin, ModelViewSetMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerialiser

    def get_permissions(self):
        if self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class KlassModelViewSet(ModelViewSetMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer

    def get_permissions(self):
        if self.action == "list":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class SessionModelViewSet(ModelViewSetMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_permissions(self):
        if self.action == "list":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]
