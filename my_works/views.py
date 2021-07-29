from IrrigatsiyaUz.settings import LANGUAGES
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.http import Http404, HttpResponse

from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission
from rest_framework import viewsets


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

class ArticlesViewList(viewsets.ModelViewSet):
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
        serializer = ArticlesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)    

class BooksViewList(viewsets.ModelViewSet):
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
        serializer = BooksSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class PresentationsViewList(viewsets.ModelViewSet):
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
        serializer = PresentationsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class ProjectsViewList(viewsets.ModelViewSet):
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
        serializer = ProjectsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class EventsViewList(viewsets.ModelViewSet):
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
        serializer = EventsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

from django.utils.translation import get_language, activate, gettext
from django.conf import settings



class VideosViewList(viewsets.ModelViewSet):
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
        serializer = VideosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)