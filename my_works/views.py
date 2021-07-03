from django.shortcuts import render, get_object_or_404
from rest_framework import serializers, status
from .models import MyWorks
from .serializers import MyWorksSerializers
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.http import Http404

from rest_framework import permissions, pagination
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import viewsets
from .paginations import CustomPagination

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True

        return object.author == request.user


class WorksViewList(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]    
    queryset = MyWorks.objects.all().order_by('-date_updated')
    serializer_class = MyWorksSerializers
    pagination_class = CustomPagination
 
    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(MyWorks, slug=work)

    def list(self, request):
        serializer = MyWorksSerializers(self.queryset, many=True)
        return Response(serializer.data)
 
    def create(self, request):
        serializer = MyWorksSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     work = get_object_or_404(self.queryset, pk=pk)
    #     serializer = MyWorksSerializers(work)
    #     return Response(serializer.data)

    # def destroy(self, request, pk=None):
    #     work = get_object_or_404(self.queryset, pk=pk)
    #     work.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



class MyWorksView(APIView):
    
    pagination_class = PageNumberPagination
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, *args, **kwargs):
        qs = MyWorks.objects.all()
        serializers = MyWorksSerializers(qs, many=True)
        return Response(serializers.data, status=200)
        
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = MyWorksSerializers(data=request.data)
        
        if serializer.is_valid():
            # category = serializer.data.get('category')
            # name = serializer.data.get('name')
            # file = serializer.data.get('file')
            # link = serializer.data.get('link')
            # date_published = serializer.data.get('date_published')
            # author = serializer.data.get('category')
            # category = serializer.data.get('category')
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors)

class MyWorksDetail(APIView):

    parser_classes = [MultiPartParser, FormParser]


    def get_object(self, pk):
        try:
            return MyWorks.objects.get(id=pk)
        except MyWorks.DoesNotExist:
            return Http404
    
    def get(self,request, pk, **args):
        work = self.get_object(pk)
        serializer = MyWorksSerializers(work, many=False)
        return Response(serializer.data)

    def put(self, request, pk, **kwargs):
        work = self.get_object(pk)

        serializer = MyWorksSerializers(work, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, pk):
        work = self.get_object(pk)
        work.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

