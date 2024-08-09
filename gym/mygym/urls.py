from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginViewSet, SignupViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'login', LoginViewSet)
router.register(r'signup', SignupViewSet)
router.register(r'userprofile', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
