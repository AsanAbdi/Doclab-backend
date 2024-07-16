from django.urls import path, include
from rest_framework import routers

from .views import AnalyzeAPIView

router = routers.DefaultRouter()

router.register('analyzes', AnalyzeAPIView, basename='analyzes')

urlpatterns = [
    path('', include(router.urls))
]