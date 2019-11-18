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
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate


class HomeView(viewsets.ModelViewSet):

        queryset = UserProfiles.objects.all()
        serializer_class = UserProfilesSerializers



        def create(self, request):

           serializer = self.serializer_class(data = request.data)

           serializer.is_valid(raise_exception = True)
           user = UserProfiles.objects.create(first_name = serializer.data.get('first_name'),username = serializer.data.get('username'),
                  email = serializer.data.get('email'))
           user.set_password(serializer.data.get('password'))
           user.save()
           return Response({'success':True,'message':"signup done"})



class LoginView(viewsets.ViewSet):


        serializer_class = LoginSerializers

        def create(self, request):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            auth = authenticate(request,username=username, password=password)
            if auth is not None:
               token = Token.objects.get(user=auth)
               print("token", token)

               return Response({'success':True, 'message':'successful','token':token.key})
            else:
                return Response({'success':False, 'message':'login unsuccessful'})






























