from django.shortcuts import render
from django.http import HttpResponse,Http404
import json
from .models import UserProfiles, Recipe, Slider, Recipe, Ingredients, Feature, FooterImage, Contact, SocialLinks, Newsletter, Address, Comments, Rating
from . serializers import UserProfilesSerializers,LoginSerializers, ContactSerializers, RecipeSerializers, IngredientSerializers, SliderSerializers, SocialLinksSerializers, FooterImageSerializers, FeatureSerializers, NewsletterSerializers,AddressSerializers,CommentSerializers,RatingSerializers,RecipePostSerializers,CommentlistSerializers,CommentUpdateSerializers,RatingListSerializers,LogoutSerializers,SocialLoginSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
import math
import json
from requests.exceptions import HTTPError
from social_django.utils import load_strategy, load_backend
from social_core.backends.oauth import BaseOAuth2
from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden


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


class SocialLoginView(viewsets.ModelViewSet):

    serializer_class = SocialLoginSerializer
    permission_classes = [AllowAny]

    def create(self, request):

        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception  =  True)
        provider = serializer.data.get('provider')
        strategy = load_strategy(request)
        try :
            backend = load_backend(strategy = strategy , name = provider, redirect_uri =None)
        except MissingBackend:
            return Response('please provide a valid provider')
            status = status.HTTP_404_BAD_REQUEST


        try:
            if isinstance(backend, BaseOAuth2):
                access_token = serializer.data.get('access_token')
            user = backend.do_auth(access_token)
        except HTTPError as error:
            return Response({
                "error": {
                    "access_token": "Invalid token",
                    "details": str(error)
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        except AuthTokenError as error:
            return Response({
                "error": "Invalid credentials",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            authenticated_user = backend.do_auth(access_token, user=user)

        except HTTPError as error:
            return Response({
                "error": "invalid token",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)

        except AuthForbidden as error:
            return Response({
                "error": "invalid token",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)

        if authenticated_user and authenticated_user.is_active:
            # generate JWT token
            login(request, authenticated_user)
            data = {
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )}
            # customize the response to your needs
            response = {
                "email": authenticated_user.email,
                "username": authenticated_user.username,
                "token": data.get('token')
            }
            return Response(status=status.HTTP_200_OK, data=response)


class LogoutView(viewsets.ModelViewSet):

    model = Token
    serializer_class =  LogoutSerializers


    def get_queryset(self):

        name = self.request.user
        print("---------",name)
        queryset = Token.objects.get(user = name)
        print("----------->>>",queryset)
        #self.request.user.token.key.delete()
        return queryset.key



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
   permission_classes = [IsAuthenticated]
   serializer_class = RecipeSerializers



class RecipePostView(viewsets.ModelViewSet):

    serializer_class = RecipePostSerializers

    def create(self, request):

        recipe_dict ={}
        recipe_list = []
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        recipe_name = serializer.data.get('recipe_name')
        print(recipe_name)
        type = serializer.data.get('type')
        category = serializer.data.get('category')

        recipe = Recipe.objects.filter(Q(category__contains=category)| Q(type__contains=type) | Q(recipe_name__contains=recipe_name))
        print("query-----", recipe)
        for data in recipe:

            recipe_dict['name'] = data.recipe_name
            recipe_dict['image'] = data.recipe_image
            print(recipe_dict)
            recipe_list.append(recipe_dict['name'])
            recipe_list.append(recipe_dict['image'])

        return Response({'data' : str(recipe_list)})


class SliderView(viewsets.ModelViewSet):

    queryset = Slider.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SliderSerializers


class SocialLinkView(viewsets.ModelViewSet):

    queryset = SocialLinks.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SocialLinksSerializers


class FooterImageView(viewsets.ModelViewSet):

    queryset = FooterImage.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FooterImageSerializers


class FeatureView(viewsets.ModelViewSet):

    queryset = Feature.objects.all()
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializers


class CommentsView(viewsets.ModelViewSet):

    serializer_class = CommentSerializers

    def create(self, request):

        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = self.request.user
        msg = serializer.data.get('msg')
        subject = serializer.data.get('subject')
        recipename =serializer.data.get('receipe_name_id')
        print("----------", recipename)
        comment = Comments(name = user, msg = msg, subject = subject, receipe_name_id = recipename)
        comment.save()
        return Response({'sucess': True, 'message': 'submitted'})




class CommentListView(viewsets.ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentlistSerializers
    permission_classes = [IsAuthenticated]


class CommentUpdateView(viewsets.ModelViewSet):

      http_method_names = ['patch' ,  'delete']
      serializer_class = CommentUpdateSerializers

      def partial_update(self, request, pk):
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception = True)
            id = serializer.data.get('id')
            name = self.request.user.username
            msg = serializer.data.get('msg')
            subject = serializer.data.get('subject')
            comment_update = Comments.objects.get(id = id)
            comment_update.msg = msg
            comment_update.subject = subject
            comment_update.save()
            return Response({'success': True, 'message': 'updated'})


      def delete(self, request , pk):

            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            id = serializer.data.get('id')
            comment_delete = Comments.objects.get(id=id)
            comment_delete.delete()
            return Response({'success': True, 'message' : 'deleted'})

class RatingListView(viewsets.ModelViewSet):

    queryset = Rating.objects.values('recipename', 'rate' , 'avg' ).distinct()
    serializer_class = RatingListSerializers


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
            rate = Rating(rate = rating, recipename = recipename,  name = name, avg = rating, total = rating)
            rate.save()
        elif(count >= 1):
            print("inside 2")

            rate_insert = Rating(rate = rating, recipename = recipename,  name = name )
            rate_insert.save()
            count1 = Rating.objects.filter(recipename=recipename).count()
            print(count1)
            r = Rating.objects.filter(recipename = recipename)
            for i in r:
                rate_sum = rate_sum + int(i.rate)
                average = rate_sum/count1

                Rating.objects.filter(recipename = recipename).update(avg = average)
                Rating.objects.filter(recipename = recipename).update(total = rate_sum)
                Rating.objects.filter(recipename = recipename).update(recipename = recipename)

        return Response({'success': True, 'message' : 'rating done'})











































