from django.urls import path, include
from .views import ProfileView, contact_view, contact_thanks
from rest_framework import routers
from django.contrib.auth import views as auth_views


router = routers.DefaultRouter()
router.register(r'',ProfileView, basename='profile')


urlpatterns = [
    path('contact/', contact_view, name='contact'),   
    path('contact/thanks/', contact_thanks, name='contact-thanks'),   

    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

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
