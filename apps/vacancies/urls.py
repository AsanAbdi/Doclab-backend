from django.urls import path, include
from rest_framework import routers

from .views import VacancyAPIView

router = routers.DefaultRouter()

router.register('vacancies', VacancyAPIView, basename='vacancies')

urlpatterns = router.urls