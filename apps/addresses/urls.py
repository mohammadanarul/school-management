from rest_framework import routers
from django.urls import path
from apps.addresses.views import CountyModelViewSet, DivisionModelViewSet

router = routers.DefaultRouter()
router.register("countries", CountyModelViewSet, basename="countries")
router.register("divisions", DivisionModelViewSet, basename="divisions")

urlpatterns = [] + router.urls
