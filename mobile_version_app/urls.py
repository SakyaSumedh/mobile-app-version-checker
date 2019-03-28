from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MobileVersionViewset, CheckVersionAPI

router = DefaultRouter()
router.register(r'mobile-version', MobileVersionViewset, base_name="mobile-version")


urlpatterns = [
    path('', include(router.urls)),
    path('check-version/', CheckVersionAPI.as_view(), name="check-version")
]
