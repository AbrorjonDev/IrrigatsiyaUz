from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages

from rest_framework.response import Response
from .serializers import ProfileSerializer
from rest_framework import permissions, generics
from rest_framework.views import APIView

from drf_writable_nested import UniqueFieldsMixin , WritableNestedModelSerializer #for updating profile 

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True

        return object.user == request.user


# def user_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST,request.FILES, instance=request.instance)

#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your Profile is Updated')
#             return redirect('profile')

#     else:
#         form = ProfileForm(instance=request.instance)
#     context = {
#         'form':form,
#     }
#     return render(request, 'profile.html', context)

# @api_view(['GET'])
# def profile(request):
#     profile = Profile.objects.get(user_id=2)
#     serializer = ProfileSerializer(profile, many=False)
#     return Response(serializer.data)


class ProfileView(generics.UpdateAPIView):
    
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer

    def get_object(self, **kwargs):
        return Profile.objects.get(user_id=2) 

    def get(self, request, **kwargs):
        profile = self.get_object()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, **kwargs):
        profile = self.get_object()
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors)


