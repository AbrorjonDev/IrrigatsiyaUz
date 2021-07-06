from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm, ContactForm
from django.contrib import messages
from django.views.generic import View


from rest_framework.response import Response
from .serializers import ProfileSerializer
from rest_framework import permissions, generics, viewsets
from rest_framework.views import APIView

from rest_framework.decorators import api_view, permission_classes
from drf_writable_nested import UniqueFieldsMixin , WritableNestedModelSerializer #for updating profile 
 

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages


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

@api_view(['GET', 'PUT'])
@permission_classes((IsOwnerOrReadOnly,))
def profile(request, format=None):
    profile = Profile.objects.get(user_id=2)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


# class ProfileView(generics.UpdateAPIView):
    
#     permission_classes = [IsOwnerOrReadOnly]
#     serializer_class = ProfileSerializer

#     def get_object(self, **kwargs):
#         return Profile.objects.get(user_id=2) 

#     def get(self, request, **kwargs):
#         profile = self.get_object()
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)

#     def put(self, request, **kwargs):
#         profile = self.get_object()
#         serializer = ProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors)
 
class ProfileView(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'put', 'head']

    def get_object(self, **kwargs):
        return Profile.objects.get(user__id=2) 

    def list(self, request, **kwargs):
        profile = self.get_object()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    

    def put(self, request, *args, **kwargs):

        profile = self.get_object()
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors)





def contact_view(request):
    if request.method=='POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            recipient_list = ['aahmadov271101@gmail.com']
            if subject and email and message:
                try:
                    message_block = f'Hey Mr.\n {subject} has sent this email message lastly.\n\n\nThis User\'s Message:\n{message}'
                    send_mail(subject, message_block, email, recipient_list)
                except BadHeaderError:
                    return messages.warning(request, 'Please try again..')
                return redirect('contact-thanks')
        else:
            messages.warning(request,'Please make sure all fields are valid')
    else:
        form = ContactForm()

    context = {
        'form':form,
    }
    return render(request, 'contact.html', context)

def contact_thanks(request):
    return HttpResponse('Thanks for your attention!We will be on contact with you.')