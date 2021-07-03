from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages

from rest_framework.response import Response
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view

def user_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=request.instance)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile is Updated')
            return redirect('profile')

    else:
        form = ProfileForm(instance=request.instance)
    context = {
        'form':form,
    }
    return render(request, 'profile.html', context)

@api_view(['GET'])
def profile(request):
    profile = Profile.objects.get(user_id=2)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


