
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from my_works.views import (
    ArticlesViewList,
    BooksViewList,
    PresentationsViewList,
    ProjectsViewList,
    EventsViewList,
    VideosViewList,
    )
from accounts.views import ProfileView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewList)
router.register(r'books', BooksViewList)
router.register(r'presentations', PresentationsViewList)
router.register(r'projects', ProjectsViewList)
router.register(r'events', EventsViewList)
router.register(r'videos', VideosViewList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProfileView.as_view(), name='profile'),   
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += router.urls


if settings.DEBUG:
    urlpatterns +=(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns +=(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

  