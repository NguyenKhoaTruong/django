from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tms', GetMethod, basename='tms')
# router.register('cluster', ClusterTms, basename='cluster')
urlpatterns = router.urls