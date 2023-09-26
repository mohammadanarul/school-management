from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from apps.helpers.mixins import DeleteModelMixin
from apps.libraries.models import Library, Book
from apps.libraries.serializers import LibrarySerializer, BookSerializer


class LibraryModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrive":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class BookModelViewSet(DeleteModelMixin, ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrive":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]
