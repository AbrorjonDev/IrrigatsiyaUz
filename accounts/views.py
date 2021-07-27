from django.shortcuts import render, redirect
from .models import Profile
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

from rest_framework.response import Response
from .serializers import ProfileSerializer
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

    def get_object(self, **kwargs):
        return Profile.objects.first() 

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
            phone = form.cleaned_data.get('phone')
            recipient_list = ['abrorjonaxmadov21@gmail.com']
            if subject and email and message:
                try:
                    message_block = f'Hey Mr.\n {subject} has sent this email message lastly.\n\n\nThis User\'s Message:\n{message}/n/n/nFor the Contact<bold>{phone}</bold>'
                    send_mail(subject, message_block, email, recipient_list)
                    contact_info = Contact.objects.create(email=email, subject=subject, phone=phone, message=message)
                    contact_info.save()
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