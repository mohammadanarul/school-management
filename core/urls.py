from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers

router = routers.DefaultRouter()
schema_view = get_schema_view(
    openapi.Info(
        title="BD Smart School Management",
        default_version="v1",
        description="BD Smart School Management api provide for frontend. It's protected and just our business purpose.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mdanarul7075@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/",
        include(
            [
                path("", include("apps.users.urls")),
                path("", include("apps.addresses.urls")),
                path("", include("apps.institutes.urls")),
                path("", include("apps.libraries.urls")),
            ]
        ),
    ),
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
