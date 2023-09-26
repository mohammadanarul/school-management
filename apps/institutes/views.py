from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.helpers.mixins import DeleteModelMixin
from apps.institutes.models import Institute, Subject, Klass, Session
from apps.institutes.serializers import (
    InstituteSerializer,
    SubjectSerialiser,
    KlassSerializer,
    SessionSerializer,
)


class InstituteModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer

    def get_permissions(self):
        if self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class SubjectModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerialiser

    def get_permissions(self):
        if self.action == "retrieve":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class KlassModelViewSet(ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer

    def get_permissions(self):
        if self.action == "list":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class SessionModelViewSet(ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_permissions(self):
        if self.action == "list":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]
