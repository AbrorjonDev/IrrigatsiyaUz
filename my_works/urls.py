from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from .views import (
    ArticlesViewList,
    BooksViewList,
    PresentationsViewList,
    ProjectsViewList,
    EventsViewList,
    VideosViewList,
    home,
    )
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'articles', ArticlesViewList, basename='articles')
router.register(r'books', BooksViewList, basename='books')
router.register(r'presentations', PresentationsViewList, basename='presentations')
router.register(r'projects', ProjectsViewList, basename='projects')
router.register(r'events', EventsViewList, basename='events')
router.register(r'videos', VideosViewList, basename='videos')

urlpatterns = [
    path('home/', home, name="home"),
]

urlpatterns += router.urls
