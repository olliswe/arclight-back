from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, current_user
from django.urls import path
from .views import CustomAuthToken

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    url(
        r"^password_reset/",
        include(
            "custom_packages.django_rest_passwordreset.urls", namespace="password_reset"
        ),
    ),
    url(r"", include(router.urls)),
    path("current_user/", current_user),
    url(r"^api-token-auth/", CustomAuthToken.as_view()),
]
