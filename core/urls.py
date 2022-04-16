from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title = "Xpovi API",
        default_version = "V1",
        description = "Test Description",
        terms_of_service = "https://www.xpovi.com/policies/terms/",
        contact = openapi.Contact(email="contact@xpovi.local"),
        license = openapi.License(name="Test License"),
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Swagger 
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # API Endpoints
    path('api/users/', include(('accounts.urls', 'accounts'), namespace='users-api')),
    path('api/business-plan/', include(('business_plan.urls', 'business_plan'), namespace='business-plan-api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
