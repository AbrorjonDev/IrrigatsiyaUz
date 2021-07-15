from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='v1',
      description="API urls description",
      terms_of_service="https://www.myblogs.com/policies/terms/",
      contact=openapi.Contact(email="aahmadov271101@gmail.com"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [


]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_works.urls')),
    path('me/', include('accounts.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns+= (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns+= (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

admin.site.site_header = 'Alimardon Mustafoqulov Administration'
admin.site.site_title = 'Administration Panel'
admin.site.index_title = 'Administration page'
