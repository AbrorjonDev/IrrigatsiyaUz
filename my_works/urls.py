from django.urls import path, include
from .views import MyWorksView, MyWorksDetail, WorksViewList
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'myworks', WorksViewList)
urlpatterns = router.urls


# urlpatterns = [
#     path('', MyWorksView.as_view(), name='my-works' ),
#     path('<int:pk>/', MyWorksDetail.as_view(), name='work-detail' ),
# ]