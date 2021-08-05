from IrrigatsiyaUz.settings import LANGUAGES
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission

from django.http import FileResponse
from rest_framework import viewsets, renderers
from rest_framework.decorators import action

class PassthroughRenderer(renderers.BaseRenderer):
    """
        Return data as-is. View should supply a Response.
    """
    media_type = ''
    format = ''
    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data

from .models import (
    Articles,
    Books, 
    Presentations,
    Projects, 
    Events,
    Videos,
    )

from .serializers import (
    ArticlesSerializers,
    BooksSerializers,
    PresentationsSerializers,
    ProjectsSerializers,
    EventsSerializers,
    VideosSerializers,
    )


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True

        return object.author == request.user

class ArticlesViewList(viewsets.ModelViewSet, viewsets.ReadOnlyModelViewSet):
    permission_classes = [ IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]    
    queryset = Articles.objects.all().order_by('-date_updated')
    serializer_class = ArticlesSerializers

    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Articles, slug=work)

    def list(self, request):
        serializer = ArticlesSerializers(Articles.objects.all().order_by('-date_updated'), many=True)
        return Response(serializer.data)
 
 
    def create(self, request):
        try:
            serializer = ArticlesSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            if e == 'UNIQUE constraint failed: my_works_articles.slug':
                return Response(_('This name is taken.Choose other one'))
            return Response(_('Some problems.Please, Try again.'))    
    
    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download(self, *args, **kwargs):
        instance = self.get_object()

        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.file.open()

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response
class BooksViewList(viewsets.ModelViewSet, viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Books.objects.all().order_by('-date_updated')
    serializer_class = BooksSerializers

    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Books, slug=work)

    def list(self, request):
        serializer = BooksSerializers(Books.objects.all().order_by('-date_updated'), many=True)
        return Response(serializer.data, status=200)
 
 
    def create(self, request):
        try:
            serializer = BooksSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            if e == 'UNIQUE constraint failed: my_works_books.slug':
                return Response(_('This name is taken.Choose other one'))
            return Response(_('Some problems.Please, Try again.'))
    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download(self, *args, **kwargs):
        instance = self.get_object()

        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.file.open()

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response

class PresentationsViewList(viewsets.ModelViewSet, viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Presentations.objects.all().order_by('-date_updated')
    serializer_class = PresentationsSerializers
 
    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Presentations, slug=work)

    def list(self, request):
        serializer = PresentationsSerializers(Presentations.objects.all().order_by('-date_updated'), many=True)
        return Response(serializer.data, status=200)

    def create(self, request):
        try:
            serializer = PresentationsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            if e == 'UNIQUE constraint failed: my_works_presentations.slug':
                return Response(_('This name is taken.Choose other one'))
            return Response(_('Some problems.Please, Try again.'))
    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download(self, *args, **kwargs):
        instance = self.get_object()

        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.file.open()

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response

class ProjectsViewList(viewsets.ModelViewSet, viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Projects.objects.all().order_by('-date_updated')
    serializer_class = ProjectsSerializers
 
    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Projects, slug=work)

    def list(self, request):
        serializer = ProjectsSerializers(Projects.objects.all().order_by('-date_updated'), many=True)
        return Response(serializer.data, status=200)
 
 
    def create(self, request):
        try:
            serializer = ProjectsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            if e == 'UNIQUE constraint failed: my_works_projects.slug':
                return Response(_('This name is taken.Choose other one'))
            return Response(_('Some problems.Please, Try again.'))

    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download(self, *args, **kwargs):
        instance = self.get_object()

        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.file.open()

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response

class EventsViewList(viewsets.ModelViewSet, viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Events.objects.all().order_by('-date_updated')
    serializer_class = EventsSerializers
 
    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Events, slug=work)

    def list(self, request):
        serializer = EventsSerializers(Events.objects.all().order_by('-date_updated'), many=True)
        return Response(serializer.data)
 
 
    def create(self, request):
        try:
            serializer = EventsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            if e == 'UNIQUE constraint failed: my_works_events.slug':
                return Response(_('This name is taken.Choose other one'))
            return Response(_('Some problems.Please, Try again.'))

    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download(self, *args, **kwargs):
        instance = self.get_object()

        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.file.open()

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response

class VideosViewList(viewsets.ModelViewSet, viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Videos.objects.all().order_by('-date_updated')
    serializer_class = VideosSerializers
 
    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Videos, slug=work)

    def list(self, request):
        serializer = VideosSerializers(Videos.objects.all().order_by('-date_updated'), many=True)
        return Response(serializer.data)
     
    def create(self, request):
        try:
            serializer = VideosSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            if e == 'UNIQUE constraint failed: my_works_videos.slug':
                return Response(_('This name is taken.Choose other one'))
            return Response(_('Some problems.Please, Try again.'))
    
    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download(self, *args, **kwargs):
        instance = self.get_object()

        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.file.open()

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response
    