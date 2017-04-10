from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from accounts.views import GroupViewSet, UserViewSet, PermissionViewSet


router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
