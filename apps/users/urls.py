from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from apps.users import views

user_routers = routers.DefaultRouter()
user_routers.register("students", views.StudentModelViewSet, basename="students")
user_routers.register("staffs", views.StaffModelViewSet, basename="staffs")


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + user_routers.urls
