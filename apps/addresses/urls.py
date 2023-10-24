from rest_framework import routers
from apps.addresses.views import (
    CountyModelViewSet,
    DivisionModelViewSet,
    DistrictModelViewSet,
    SubDistrictModelViewSet,
    UnionModelViewSet,
    WardModelViewSet,
    AddressModelViewSet,
)

router = routers.DefaultRouter()
router.register("countries", CountyModelViewSet, basename="countries")
router.register("divisions", DivisionModelViewSet, basename="divisions")
router.register("districts", DistrictModelViewSet, basename="districts")
router.register("sub_districts", SubDistrictModelViewSet, basename="sub_districts")
router.register("unions", UnionModelViewSet, basename="unions")
router.register("wards", WardModelViewSet, basename="wards")
router.register("addresses", AddressModelViewSet, basename="addresses")
urlpatterns = [] + router.urls
