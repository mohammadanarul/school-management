from rest_framework.mixins import DestroyModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status


class ModelViewSetMixin(ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(created_by_id=self.request.user.id, updated_by_id=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save(updated_by_id=self.request.user.id)


class DeleteModelMixin(DestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if user.is_authenticated:
            if user.is_staff or user.is_superuser:
                self.perform_destroy(instance)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(
                    {"message": "sorry, not acceptable"},
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )
        else:
            return Response({"message": "unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
