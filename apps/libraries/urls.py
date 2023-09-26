from rest_framework import routers
from apps.libraries.views import LibraryModelViewSet, BookModelViewSet

library_routers = routers.DefaultRouter()
library_routers.register("libraries", LibraryModelViewSet, basename="libraries")
library_routers.register("books", BookModelViewSet, basename="books")

urlpatterns = [] + library_routers.urls
