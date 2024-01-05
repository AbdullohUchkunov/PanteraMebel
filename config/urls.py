from django.contrib import admin
from django.urls import path,re_path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


class JWTSchemaGenerator(OpenAPISchemaGenerator):
    def get_security_definitions(self):
        security_definitions = super().get_security_definitions()
        security_definitions['Bearer'] = {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
        return security_definitions


schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1',
        description='E-commerce API',
        terms_of_service='https://www.google.com',
        contact=openapi.Contact(email='mebelpantera300@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=JWTSchemaGenerator,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0),name='schema-json'),
    path('',schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    *i18n_patterns(*urlpatterns,prefix_default_language=False)
]