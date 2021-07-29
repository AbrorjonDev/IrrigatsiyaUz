from django.urls import path, include
from .views import ContactAPIView, ProfileView, AdminContactView, AddressLinkView
from rest_framework import routers
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'phones',AdminContactView, basename='phone')
router.register(r'addresses',AddressLinkView, basename='addresses')
router.register(r'contact',ContactAPIView, basename='contact')
router.register(r'',ProfileView, basename='profile')


urlpatterns = [
    path('auth-token/', obtain_auth_token, name='token-auth'),
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
