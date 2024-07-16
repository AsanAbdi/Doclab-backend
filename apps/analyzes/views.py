from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import AnalyzeSerializer
from .models import Analyze

# Create your views here.
class AnalyzeAPIView(ModelViewSet):
    queryset = Analyze.objects.all()
    serializer_class = AnalyzeSerializer