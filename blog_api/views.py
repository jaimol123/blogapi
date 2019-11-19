from django.shortcuts import render
from django.http import HttpResponse,Http404
import json
from .models import UserProfiles, Recipe, Slider, Recipe, Ingredients, Feature, FooterImage, Contact, SocialLinks, Newsletter, Address
from . serializers import UserProfilesSerializers,LoginSerializers, ContactSerializers, RecipeSerializers, IngredientSerializers, SliderSerializers, SocialLinksSerializers, FooterImageSerializers, FeatureSerializers, NewsletterSerializers,AddressSerializers
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



class ContactView(viewsets.ViewSet):

    serializer_class = ContactSerializers

    def create(self, request):

        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        contact_name = serializer.data.get('contact_name')
        contact_email = serializer.data.get('contact_email')
        contact_msg = serializer.data.get('contact_msg')
        contact_subject = serializer.data.get('contact_subject')
        contact = Contact(contact_name = contact_name, contact_email = contact_email, contact_msg = contact_msg, contact_subject = contact_subject)
        contact.save()
        return Response({'sucess':True, 'message': 'message submitted'})


class RecipeView(viewsets.ModelViewSet):

   queryset = Recipe.objects.all()
   serializer_class = RecipeSerializers


class SliderView(viewsets.ModelViewSet):

    queryset = Slider.objects.all()
    serializer_class = SliderSerializers


class SocialLinkView(viewsets.ModelViewSet):

    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinksSerializers


class FooterImageView(viewsets.ModelViewSet):

    queryset = FooterImage.objects.all()
    serializer_class = FooterImageSerializers


class FeatureView(viewsets.ModelViewSet):

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializers


class NewsletterView(viewsets.ModelViewSet):

    serializer_class = NewsletterSerializers

    def create(self, request):

        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        mail = serializer.data.get('mail')
        newsletter = Newsletter(mail = mail)
        newsletter.save()
        return Response({'sucsess':True, 'message': 'subscribed'})

class AddressView(viewsets.ModelViewSet):

    queryset = Address.objects.all()
    serializer_class = AddressSerializers






































