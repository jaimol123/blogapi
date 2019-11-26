from django.conf.urls import url
from django.urls import path,include
from rest_framework import routers
from . views import HomeView, LoginView, ContactView, RecipeView,  SliderView, SocialLinkView, FooterImageView,FeatureView, NewsletterView,AddressView,CommentsView, RatingView,RecipePostView,CommentListView,CommentUpdateView,RatingListView,RatingListView,LogoutView,SocialLoginView
from . import views

router = routers.DefaultRouter()
router.register(r'rate-list-view' , RatingListView , basename = 'recipe-list'),
router.register(r'rate-post' , RatingView , basename = 'rating'),

router.register(r'comment-update' , CommentUpdateView, basename = 'comment_update'),
router.register(r'comment-list', CommentListView, basename = 'comment_list'),
router.register(r'comment-post', CommentsView, basename = 'comment'),

router.register(r'recipe-post', RecipePostView , basename = 'recipe_post'),
router.register(r'recipe-list', RecipeView, basename = 'recipe')

router.register(r'address-list', AddressView, basename = 'address'),
router.register(r'newsletter-post', NewsletterView, basename = 'newsletter')
router.register(r'feature-list', FeatureView , basename = 'feature')
router.register(r'footerimage-list', FooterImageView, basename = 'footerimage')
router.register(r'socialLinks-list', SocialLinkView, basename = 'socialLinks')
router.register(r'slider-list', SliderView, basename = 'slider')
router.register(r'contact-post', ContactView, basename = 'contact')

router.register(r'social-login' , SocialLoginView , basename = 'social-login')
router.register(r'logout-list', LogoutView, basename = 'logout')
router.register(r'login-post', LoginView, basename = 'login-post')
router.register(r'',  HomeView, basename = 'home')





urlpatterns = [
                    url(r'', include(router.urls)),


              ]




