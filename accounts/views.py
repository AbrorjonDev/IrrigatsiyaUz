from django.shortcuts import render, redirect
from .models import Profile
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

from rest_framework.response import Response
from .serializers import ContactSerializer, ProfileSerializer
from rest_framework import permissions, viewsets

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True

        return object.user == request.user

class ProfileView(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'put', 'head']
    queryset = Profile.objects.all()

    def get_object(self, **kwargs):
        return Profile.objects.first() 

    def retrieve(self, request, **kwargs):
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
class ContactAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ContactSerializer
    http_method_names = ['post', 'head']

    def create(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            subject = serializer.validated_data.get('subject')
            email = serializer.validated_data.get('email')
            message = serializer.validated_data.get('message')
            phone = serializer.validated_data.get('phone')
            recipient_list = ['abrorjonaxmadov21@gmail.com']
            if subject and email and phone and message:
                try:
                    message_block = f'Hey Mr.\n {subject} has sent this email message lastly.\n\n\nThis User\'s Message:\n{message}/n/n/nFor the Contact<bold>{phone}</bold>'
                    send_mail(subject, message_block, email, recipient_list)
                    contact_info = Contact.objects.create(email=email, subject=subject, phone=phone, message=message)
                    contact_info.save()
                except BadHeaderError:
                    return messages.warning(request, 'Please try again..')
                Response({'response':'E\'tiboringiz uchun rahmat!Tez orada siz bilan bog\'lanamiz..'})

        return Response({'response':'Xabar jo\'natildi.'})