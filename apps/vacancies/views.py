from rest_framework.viewsets import ModelViewSet

from .serializers import VacancySerializer
from .models import Vacancy

# Create your views here.
class VacancyAPIView(ModelViewSet):
    queryset = Vacancy.objects.filter(is_actual=True)
    serializer_class = VacancySerializer