from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, current_user
from django.urls import path
from .views import CustomAuthToken

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"", include(router.urls)),
    path("current_user/", current_user),
    url(r"^api-token-auth/", CustomAuthToken.as_view()),
]
