from django.urls import path
from .views import MyWorksView, MyWorksDetail

urlpatterns = [
    path('', MyWorksView.as_view(), name='my-works' ),
    path('<int:pk>/', MyWorksDetail.as_view(), name='work-detail' ),

]