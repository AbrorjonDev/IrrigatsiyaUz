
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views
    

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

    path('password-reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]

urlpatterns += router.urls


if settings.DEBUG:
    urlpatterns +=(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns +=(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

  