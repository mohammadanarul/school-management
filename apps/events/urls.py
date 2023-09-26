from rest_framework import routers
from apps.events.views import EventModelViewSet

event_routers = routers.DefaultRouter()
event_routers.register("events", EventModelViewSet, basename="events")

urlpatterns = [] + event_routers.urls
