from django.shortcuts import render
from django.http import HttpResponse,Http404
import json
from .models import UserProfiles, Recipe, Slider, Recipe, Ingredients, Feature, FooterImage, Contact, SocialLinks, Newsletter, Address, Comments, Rating
from . serializers import UserProfilesSerializers,LoginSerializers, ContactSerializers, RecipeSerializers, IngredientSerializers, SliderSerializers, SocialLinksSerializers, FooterImageSerializers, FeatureSerializers, NewsletterSerializers,AddressSerializers,CommentSerializers,RatingSerializers,RecipePostSerializers,CommentlistSerializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.generics import GenricAPIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
from django.db.models import Q
import math
import json


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

        def update(self, request):
                instance = self.get_object()
                instance.first_name = request.data.get('first_name')
                instance.save()
                serializer = self.serializer_class(instance)
                serializer.is_valid(raise_exception = True)
                self.perform_update(serializer)
                return Response(serializer.data)

        def perform_update(self, instance):
            instance.update()



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




class RecipePostView(viewsets.ModelViewSet):

    serializer_class = RecipePostSerializers

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        recipe_name = serializer.data.get('recipe_name')
        type = serializer.data.get('type')
        category = serializer.data.get('category')
        recipe = Recipe.objects.filter(Q(category__contains=category)).filter(Q(type__contains=type)).filter(Q(recipe_name__contains=recipe_name))
        return Response({'success': True, 'data' : str(recipe)})


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


class CommentsView(viewsets.ModelViewSet):

    serializer_class = CommentSerializers

    def create(self, request):

        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = self.request.user
        msg = serializer.data.get('msg')
        subject = serializer.data.get('subject')
        recipename =serializer.data.get('receipe_name')
        print("----------", recipename)
        comment = Comments(name = user, msg = msg, subject = subject, receipe_name_id = recipename)
        comment.save()
        return Response({'sucess': True, 'message': 'submitted'})


class CommentListView(viewsets.ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentlistSerializers





class RatingView(viewsets.ModelViewSet):

    serializer_class = RatingSerializers


    def create(self, request):
        rate_sum=0
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        rating = serializer.data.get('rate')
        recipename = serializer.data.get('recipe_name')
        rimage = Recipe.objects.get(recipe_name = recipename)
        rimg = rimage.recipe_image
        name = self.request.user
        print(name)
        count = Rating.objects.filter(recipename = recipename).count()
        if(count < 1):
            print("inside 1")
            rate = Rating(rate = rating, recipename = recipename, recipeimage = rimg, name = name)
            rate.save()
        elif(count >= 1):
            print("inside 2")

            rate_insert = Rating(rate = rating, recipename = recipename, recipeimage = rimg , name = name )
            rate_insert.save()
            count1 = Rating.objects.filter(recipename=recipename).count()
            print(count1)
            r = Rating.objects.filter(recipename = recipename)
            for i in r:
                rate_sum = rate_sum + int(i.rate)
                average = rate_sum/count1
            print("values-----------",rate_sum, average)
            Rating.objects.filter(recipename = recipename).update(avg = average)
            Rating.objects.filter(recipename=recipename).update(total = rate_sum)

        return Response({'success': True, 'message' : 'rating done'})









































