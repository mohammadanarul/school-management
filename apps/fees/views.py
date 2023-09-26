from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.fees.models import Fee
from apps.fees.serializers import FeeSerializer


class FeeModelViewSet(ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer
