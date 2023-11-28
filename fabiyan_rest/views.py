from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from .serializers import *


@api_view(['GET'])
def get_page2(request):
    profile = Profile.objects.all()
    serializer = ProfileRestSerializers(profile, many=True)

    return Response(serializer.data)

