from django.shortcuts import render
from django.http import HttpResponse,Http404
import json
from .models import UserProfiles, Recipe, Slider
from . serializers import UserProfilesSerializers,LoginSerializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser




class HomeView(generics.ListCreateAPIView):

        queryset = UserProfiles.objects.all()
        serializer_class = UserProfilesSerializers
        permission_classes = [IsAdminUser]


class LoginView(generics.CreateAPIView):

        queryset = UserProfiles.objects.all()
        serializer_class = LoginSerializers
       

























