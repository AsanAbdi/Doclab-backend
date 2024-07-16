from django.urls import path, include
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from apps.analyzes.serializers import AnalyzeSerializer
from apps.vacancies.serializers import VacancySerializer
from apps.posts.serializers import PostSerializer

api_v1_patterns = [
    path("", include("apps.analyzes.urls")),
    path("", include("apps.posts.urls")),
    path("", include("apps.vacancies.urls"))
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_v1_patterns))
]

schema_view = get_schema_view(
    openapi.Info(
        title="Doclab Laboratory",
        default_version='v1',
        description="API for Doclab",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="asanabdi50@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns += [
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

schema_view.serializer_mapping = {
    'Analyze': AnalyzeSerializer,
    'Post': PostSerializer,
    'Vacancy': VacancySerializer,
}
