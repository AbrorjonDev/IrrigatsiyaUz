from django.shortcuts import render, get_object_or_404
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.http import Http404

from rest_framework import permissions, pagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission
from rest_framework import viewsets
from .paginations import CustomPagination

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


class PaginationClass(PageNumberPagination):
    page_query_param = 'p'
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class ArticlesViewList(viewsets.ModelViewSet):
    permission_classes = [ IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]    
    queryset = Articles.objects.all().order_by('-date_updated')
    serializer_class = ArticlesSerializers
    pagination_class = CustomPagination

    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Articles, slug=work)

    def list(self, request):
        pagination = PaginationClass()
        results = pagination.paginate_queryset(self.queryset, request) 
        serializer = ArticlesSerializers(results, many=True)
        return pagination.get_paginated_response(serializer.data)
 
 
    def create(self, request):
        serializer = ArticlesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)    

class BooksViewList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Books.objects.all().order_by('-date_updated')
    serializer_class = BooksSerializers
    pagination_class = CustomPagination
 
    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Books, slug=work)

    def list(self, request):
        pagination = PaginationClass()
        results = pagination.paginate_queryset(self.queryset, request) 
        serializer = BooksSerializers(results, many=True)
        return pagination.get_paginated_response(serializer.data)
 
 
    def create(self, request):
        serializer = BooksSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class PresentationsViewList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Presentations.objects.all().order_by('-date_updated')
    serializer_class = PresentationsSerializers
    pagination_class = CustomPagination
 
    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Presentations, slug=work)

    def list(self, request):
        pagination = PaginationClass()
        results = pagination.paginate_queryset(self.queryset, request) 
        serializer = PresentationsSerializers(results, many=True)
        return pagination.get_paginated_response(serializer.data)
 
 
    def create(self, request):
        serializer = PresentationsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class ProjectsViewList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Projects.objects.all().order_by('-date_updated')
    serializer_class = ProjectsSerializers
    pagination_class = CustomPagination
 
    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Projects, slug=work)

    def list(self, request):
        pagination = PaginationClass()
        results = pagination.paginate_queryset(self.queryset, request) 
        serializer = ProjectsSerializers(results, many=True)
        return pagination.get_paginated_response(serializer.data)
 
 
    def create(self, request):
        serializer = ProjectsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class EventsViewList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Events.objects.all().order_by('-date_updated')
    serializer_class = EventsSerializers
    pagination_class = CustomPagination
 
    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Events, slug=work)

    def list(self, request):
        pagination = PaginationClass()
        results = pagination.paginate_queryset(self.queryset, request) 
        serializer = EventsSerializers(results, many=True)
        return pagination.get_paginated_response(serializer.data)
 
 
    def create(self, request):
        serializer = EventsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class VideosViewList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Videos.objects.all().order_by('-date_updated')
    serializer_class = VideosSerializers
    pagination_class = CustomPagination
 
    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Videos, slug=work)

    def list(self, request):
        pagination = PaginationClass()
        results = pagination.paginate_queryset(self.queryset, request) 
        serializer = VideosSerializers(results, many=True)
        return pagination.get_paginated_response(serializer.data)
 
 
    def create(self, request):
        serializer = VideosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)